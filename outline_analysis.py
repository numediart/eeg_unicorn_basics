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

# Data Preprocessing + Feature Extraction

if not os.path.exists(os.path.join(path_save, 'feat_mat.npy')):
    # Filter Parameters Definition
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

    np.save(os.path.join(path_save, 'feat_mat'), x)
    np.save(os.path.join(path_save, 'video_label'), y)

    info = np.load('info_vid.npy', allow_pickle=True)
    y = gen_val_arousal(info, y.astype(int) )
    np.save(os.path.join(path_save, 'label'), y)

else:
    x = np.load(os.path.join(path_save, 'feat_mat.npy'))
    y = np.load(os.path.join(path_save, 'label.npy'))

x = x.reshape(x.shape[0], -1)

# Valence and Arousal Classifier 
plot_trees = False

# Approach Evaluation
val_score = []
aro_score = []
for i in tqdm(range(100)):
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2)
    # Valence 
    #clf = RandomForestClassifier()
    clf_valence = tree.DecisionTreeClassifier(max_depth=4)
    clf_valence.fit(x_train, y_train[:, 0])
    val_score.append(clf_valence.score(x_test, y_test[:, 0]))
    # Arousal
    #clf = RandomForestClassifier()
    clf_arousal = tree.DecisionTreeClassifier(max_depth=4)
    clf_arousal.fit(x_train, y_train[:, 1])
    aro_score.append(clf_arousal.score(x_test, y_test[:, 1]))
print("Cross Validation Accuracy for Valence Estimation: %.2f/%.1f - Arousal Estimation: %.2f/%.1f"%(100*np.mean(val_score),
    100*np.std(val_score), 100*np.mean(aro_score), 100*np.std(aro_score)))

if plot_trees:
    tree.plot_tree(clf_valence, filled=True, rounded=True, fontsize=8)
    plt.suptitle('Decision Tree Valence')
    plt.show()

    tree.plot_tree(clf_arousal, filled=True, rounded=True, fontsize=8)
    plt.suptitle('Decision Tree Arousal')
    plt.show()


clf_valence = tree.DecisionTreeClassifier(max_depth=4)
clf_valence.fit(x, y[:, 0])

clf_arousal = tree.DecisionTreeClassifier(max_depth=4)
clf_arousal.fit(x, y[:, 1])

dump(clf_arousal, os.path.join(path_save, 'clf_arousal'))
dump(clf_valence, os.path.join(path_save, 'clf_valence'))

print('The classifiers have been saved in '+path_save)