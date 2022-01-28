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
import cv2
import numpy as np

path_img = 'util_img'

img_smiley = cv2.imread(os.path.join(path_img, 'ha_lv.png'))
img_graph = cv2.imread(os.path.join(path_img, 'empty_graph.png'))

while True:
    if os.path.exists(os.path.join(path_img, 'current_smiley.png')):
        img_smiley = cv2.imread(os.path.join(path_img, 'current_smiley.png'))
    if os.path.exists(os.path.join(path_img, 'current_graph.png')):
        img_graph = cv2.imread(os.path.join(path_img, 'current_graph.png'))

    if img_smiley is not None:
        cv2.imshow('Emotion Representation - Smiley',img_smiley)
    if img_graph is not None:
        cv2.imshow('Emotion Representation - Valence/Arousal',img_graph)
        
    k=cv2.waitKey(500) & 0XFF
    if k== 27 :
        break
cv2.destroyAllWindows()
