# Introduction to EEG recording with g.tec Unicorn Hybrid

This repository proposes various codes to record and process EEG signals. Nevertheless, the codes have initially been designed for recording with the g.tec Unicorn Hybrid, the software can be adapted with other compatible EEG recorders with [OpenVibe](http://openvibe.inria.fr/supported-hardware/).

The framework proposes scripts helping to record EEG and process them. A BCI application is also provided in this repo, this last aiming to assess emotional state.

## EEG Signal Recording and Processing

The repository proposes basics to register, plot and create the first experimental procedure and database with the Unicorn Hybrid Black EEG recorder in python3. The proposed repository is composed of several scripts:

- [pylsl_intro](pylsl_intro.py) giving an introduction to handle, inspect and save EEG signals from a generic oscillator, biomedical or entertainment EEG recorder (available on [OpenVIBE](http://openvibe.inria.fr/supported-hardware/)).
- [pylsl_plot](pylsl_plot.py) giving a real-time plot of the EEG signal.
- [play_vid](play_vid.py) and [play_intro](play_intro.py) respectively playing a video or an introduction screen for the experimentation.
- [intro_interface](intro_interface.py) proposing a pipeline to create a database of EEG recording during video watching. The [registration_pipeline](registration_pipeline.py) script proposes a whole pipeline for automatic EEG segments recording and annotation.

To simulate and manage the data pipe, the python code works with [OpenVibe](http://openvibe.inria.fr/) platform. The server allows the information transfer from the recorder to python script.

## BCI for Emotion Assessment

A BCI application aiming to assess emotional state during videos is also provided. The proposed application is inspired by the works of Katsigiannis and Ramzan in [DREAMER](https://ieeexplore.ieee.org/document/7887697). The goal of the pipeline is to design tools assessing emotion in real-time, the considered steps in the design of these tools are:

1. Design of a benchmark promoting several emotional states ([benchmark](registration_pipeline.py));
2. Recording of EEG signals with the designed benchmark;
3. Analysis of EEG signals and creation of a box classifying them ([analysis](outline_analysis.py));
4. Integration of the box in a real-time recording pipeline with a feedback in function of the according to the emotional state ([integration](pylsl_emotion.py) - [feedback](play_emotion.py));
5. Let's Play! :wink:

More info about the applications LINK_TO_DEFINE

### Instructions

For the direct use of the BCI [pylsl_emotion](pylsl_emotion.py) and [play_emotion](play_emotion.py) have to be run simultaneously. The OpenVibe server must also be launched for signals management. More info about the outline analysis can be found here LINK_TO_DEFINE.

To recreate a database, the considered videos have to be put in `example_vids/` directory or the path has to be corrected in [registration_pipeline](registration_pipeline.py) script. The signals will be automatically stored in `save_dir/`.

To modify the analysis part, five sessions of 20 minutes each are proposed in the `save_dir/` directory, the corresponding labels and extracted features are also provided. The proposed classifiers considered are based on [decision trees](https://scikit-learn.org/stable/modules/tree.html), however, more complex and recent approaches can be considered.

## Installation and Dependencies

### General 

- [OpenVibe v3.2.0](http://openvibe.inria.fr/downloads/)

### Python

- [Playsound](https://github.com/TaylorSMarks/playsound)

- OpenCV

- Scikit-learn

- [pylsl](https://github.com/chkothe/pylsl) 1.13.1

The packages can be installed automatically with pip: `pip install -r requirement.txt` or anaconda `conda env create -f conda_environment.yml`


## Remarks

If you are interested in our work, don't hesitate to contact us (victor.delvigne[at]umons.ac.be). 

Wish you the best in your research projects! :bowtie: