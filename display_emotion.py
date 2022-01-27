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
