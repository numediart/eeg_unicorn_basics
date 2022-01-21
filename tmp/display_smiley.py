import numpy as np
import matplotlib.pyplot as plt 

emotion = np.load('save_dir/em_smileys.npy', allow_pickle=True).all()

k = list(emotion.keys())

img = {}

for keys in k:
    img[keys] = np.zeros((32, 32))
    for coord in emotion[keys]:
        img[keys][coord[0], coord[1]] = 1
    
plt.axis('off')
for i in range(100):
    np.random.shuffle(k)
    plt.imshow(img[k[0]], cmap='binary')
    print(k[0])
    plt.pause(0.05)