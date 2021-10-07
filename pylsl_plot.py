import msvcrt
import numpy as np
import matplotlib.pyplot as plt

from pylsl import StreamInlet, resolve_stream

duration = 4
sampling_frequency = 250
down_sampling_ratio = 10
choosen_electrode = 1

plt.style.use('dark_background')

def main():
    streams = resolve_stream()
    inlet = StreamInlet(streams[0])

    aborted = False

    i = 0
    j = 0
    t = np.zeros((int(duration*sampling_frequency/down_sampling_ratio)))
    y = np.zeros((int(duration*sampling_frequency/down_sampling_ratio)))
    
    while not aborted:
        j = i//down_sampling_ratio
        sample, timestamp = inlet.pull_sample()

        if i%down_sampling_ratio==0:
            if j < int(duration*sampling_frequency/down_sampling_ratio):
                t[j] = timestamp
                y[j] = sample[choosen_electrode]
            else:
                t = np.roll(t, -1)
                y = np.roll(y, -1)
                t[-1] = timestamp
                y[-1] = sample[choosen_electrode]

                std = np.std(y)

                plt.axis([t[0]-1, t[1]+1, np.min(y)-std, np.max(y)+std])

                plt.plot(t, y, 'o-', c='c')
                plt.pause(0.05)
        i += 1
        if msvcrt.kbhit() and msvcrt.getch()[0] == 27:
            aborted = True

    plt.show()

if __name__ == '__main__':
    main()