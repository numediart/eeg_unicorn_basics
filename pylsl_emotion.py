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

import time

from utils import *
from pylsl import StreamInlet, resolve_stream

duration = 4
sampling_frequency = 50
down_sampling_ratio = 5
n_electrodes = 8


streams = resolve_stream()
inlet = StreamInlet(streams[0])

aborted = False
i = 0
j = 0

filters = [] 
freq_lim = np.asarray([
    [4, 4], #delta
    [4, 8], #theta 
    [8, 13],#alpha 
    [13, 13]]) #beta

filt_type = ['lowpass', 'bandpass', 'bandpass', 'highpass']
for f in range(freq_lim.shape[0]):
    b, a =gen_coeff(freq_lim[f], filtype=filt_type[f])
    filters.append([b, a])

sig = []

clf_arousal = load('save_dir/clf_arousal')
clf_valence = load('save_dir/clf_valence')

while not aborted:
    sample, timestamp = inlet.pull_sample()

    if i%down_sampling_ratio==0:
        x = np.asarray([sample[i] for i in range(n_electrodes)])
        sig.append(x)
        j += 1 

    if j > duration*sampling_frequency:
        sig = np.asarray(sig)
        feat = []
        t = time.time()


        feat = np.asarray([comp_feat_short(sig[:, e], filters) for e in range(n_electrodes)]).reshape(1, -1)
        arousal = clf_arousal.predict(feat)
        valence = clf_valence.predict(feat)
        print(arousal, valence)

        sig = []
        j = 0
        i = 0

    i+= 1


# 0 correspond to low and 1 to high valence/arousal