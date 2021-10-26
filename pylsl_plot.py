'''
Created by Victor Delvigne
ISIA Lab, Faculty of Engineering University of Mons, Mons (Belgium)
IMT Nord Europe, Villeneuve d'Ascq (France)
victor.delvigne@umons.ac.be
Source: TBD
Copyright (C) 2021 - UMons/IMT Nord Europe
This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.
This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.
You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
'''

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