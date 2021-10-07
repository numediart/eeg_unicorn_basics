import os
import time
import msvcrt
import datetime

from pylsl import StreamInlet, resolve_stream

def main():
    path_dir = 'save_dir'
    save_update = 5
    stream_timestamp = 1000
    streams = resolve_stream()

    inlet = StreamInlet(streams[0])

    aborted = False
    print_sample = False
    saving = False

    i = 0
    tot = ''

    while not aborted:
        
        sample, timestamp = inlet.pull_sample()
        
        if saving and i%save_update==0:
            tot += str(timestamp)
            tot += '\t'
            tot += '\t'.join(str(e) for e in sample)
            tot += '\n'

        if print_sample:
            print("Timestame %.3f \t num_sample=%d" %(timestamp, len(sample)))
        if msvcrt.kbhit() and msvcrt.getch()[0] == 27:
            aborted = True
        if msvcrt.kbhit() and msvcrt.getch()[0] == 112:
            print_sample = not print_sample
        if (msvcrt.kbhit() and msvcrt.getch()[0] == 115) or i==stream_timestamp:
            print('Start Signal Registration')
            file_name = os.path.join(path_dir, 'sig_'+datetime.datetime.now().strftime("%d_%m_%Y__%H_%M_%S")+'.txt')
            t = time.time()
            saving = not saving

        i += 1
    if saving:
        csv = open(file_name, 'w')
        csv.write(tot)
        csv.close()
    print(time.time()-t)

if __name__ == '__main__':
    main()