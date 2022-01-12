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

from utils import *

path_save = 'save_dir/'
sampling_frequency = 50

#Filter Parameters
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

x, y = sig_vid(path_save)
x, y = gen_feat(x, y, filters)
np.save('save_dir/feat_mat', x)
np.save('save_dir/video_label', y)