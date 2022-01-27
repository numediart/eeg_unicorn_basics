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

import numpy as np
import matplotlib.pyplot as plt 

emotion = np.load('../save_dir/em_smileys.npy', allow_pickle=True).all()
k = list(emotion.keys())

img = {}
for keys in k:
    img[keys] = np.zeros((32, 32))
    for coord in emotion[keys]:
        img[keys][coord[0], coord[1]] = 1
    
plt.axis('off')
for i in range(len(k)):
    plt.imshow(img[k[i]], cmap='binary')
    plt.savefig(k[i])
    plt.show()