import os
import time
import shutil

import numpy as np
import matplotlib.pyplot as plt

path = 'util_img'

fig = plt.figure(figsize=(6.25, 6.25))
r = np.linspace(-1, 1, 1000)

fontdict = {'color':  'darkred',
        'weight': 'light',
        'size': 8.5,
        }
def custom_mean(x, y, weight):
    return (x+weight*y)/(weight+1)

for i in range(100):
    valence, arousal = np.random.randint(0, 2, 2)
    if i>0:
        valence = custom_mean(old_val, valence, 3)
        arousal = custom_mean(old_ar,  arousal, 3)

    plt.plot(r, -np.sqrt(1-r**2), c='black')
    plt.plot(r, np.sqrt(1 -r**2), c='black')
    plt.arrow(0, -1.15, 0, 2.25, width=0.0085, color='black')
    plt.arrow(-1.15, 0, 2.25, 0, width=0.0085, color='black')
    plt.text(1.02, 0.075, 'Valence', fontdict)
    plt.text(0.075,1.075, 'Arousal', fontdict)
    ax = plt.gca()
    ax.set_xlim([-1.175, 1.175])
    ax.set_ylim([-1.175, 1.175])
    plt.grid(visible=True)

    ax.scatter(valence-0.5, arousal-0.5)
    plt.savefig(os.path.join(path, 'current_graph'))
    old_val = valence
    old_ar  = arousal

    if valence > 0.5:
        if arousal > 0.5:
            shutil.copy(os.path.join(path, 'ha_hv.png'), os.path.join(path, 'current_smiley.png'))
        else:
            shutil.copy(os.path.join(path, 'la_hv.png'), os.path.join(path, 'current_smiley.png'))
    elif arousal > 0.5:
        shutil.copy(os.path.join(path, 'ha_lv.png'), os.path.join(path, 'current_smiley.png'))
    else: 
        shutil.copy(os.path.join(path, 'la_lv.png'), os.path.join(path, 'current_smiley.png'))

    ax.clear()

    time.sleep(0.5)