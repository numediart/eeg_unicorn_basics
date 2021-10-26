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
from utils import *


def main():

    vid_path = '/home/vdelv/Downloads/DREAMER_VID/*.m4v'
    path_save = 'save_dir'
    vid_list = glob.glob(vid_path)

    np.random.shuffle(vid_list)
    vid_id = -1

    finished = False

    save_update = 5
    stream_timestamp = 1000
    streams = resolve_stream()
    inlet = StreamInlet(streams[0])

    sig_tot = ''
    vid_tot = ''
    i = 0
    t_b = 0
    vid_duration = 0
    while not finished:
        
        sample, timestamp = inlet.pull_sample()

        if timestamp > vid_duration + t_b:
            if vid_id == -1:
                print('Begin Record - Intro')
                vid_duration = 5
                os.system('python play_intro.py &')
                vid_id += 1
            elif vid_id == len(vid_list):
                finished = True
                print('Finish Record')
            else :
                print('Video '+str(vid_id+1))
                vid_duration = len_vid(vid_list[vid_id])
                os.system('python play_intro.py '+vid_list[vid_id]+' '+ str(vid_id+1)+ ' &')
            t_b = timestamp
            
        # Register Signal
        if i%save_update==0:
            sig_tot += str(timestamp)
            sig_tot += '\t'
            sig_tot += '\t'.join(str(e) for e in sample)
            sig_tot += '\n'

            vid_tot += str(timestamp)
            vid_tot += '\t'
            if vid_id == 0:
                vid_tot += 'intro'
            else :
                vid_tot += vid_list.split('/')[-1]
            vid_tot += '\n'

        i += 1
    date = datetime.datetime.now().strftime("%d_%m_%Y__%H_%M_%S")+'.txt'
    sig_f_name = os.path.join(path_save, 'sig_'+date)
    vid_f_name = os.path.join(path_save, 'log_'+date)

    sig_file = open(sig_f_name, 'w')
    sig_file.write(sig_tot)
    sig_file.close()

    vid_file = open(vid_f_name, 'w')
    vid_file.write(vid_tot)
    vid_file.close()
    print('Files Saved in '+path_save+'/..'+date)