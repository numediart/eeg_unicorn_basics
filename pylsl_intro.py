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