# Introduction to EEG recording with g.tec Unicorn Hybrid

This repository proposes various codes to record and process EEG signals. Nevertheless, the codes have initially been designed for recording with the g.tec Unicorn Hybrid, the software can be adapted with other compatible EEG recorder with [OpenVibe](http://openvibe.inria.fr/supported-hardware/).

The framework proposes scripts helping to record EEG and process them. A BCI application is also provided in this repo, this last aiming to assess emotion state.

## EEG Signal Recording and Processing

The repository proposes basics to register, plot and create the first experimental procedure and database with the Unicorn Hybrid Black EEG recorder in python3. The proposed repository is composed of several scripts:

- [pylsl_intro](pylsl_intro.py) giving an introduction to handle, inspect and save EEG signals from generic oscillator, biomedical or entertainment EEG recorder (available on [OpenVIBE](http://openvibe.inria.fr/supported-hardware/)).
- [pylsl_plot](pylsl_plot.py) giving a real time plot of the EEG signal.
- [play_vid](play_vid.py) and [play_intro](play_intro.py) respectively playing a video or an introduction screen for the experimentation.
- [intro_interface](intro_interface.py) proposing a pipeline to create a database of EEG recording during videos watching. The [registration_pipeline](registration_pipeline.py) script proposes a whole pipeline for automatic EEG segements recording and annotation.

To simulate and manage the data pipe, the python code works with [OpenVibe](http://openvibe.inria.fr/) platform. The server allows the information transfer from recorder to python script.

## BCI for Emotion Assessments

blabla blab a BCI can be designed and described in the following blog post. The considered steps are :
1. a 
2. b
3. c 
4. d 
5. e


Katsigiannis and Ramzan in [DREAMER](https://ieeexplore-ieee-org.ressources-electroniques.univ-lille.fr/document/7887697). This last consisting to an EEG signals recorded during watching of video promoting specific emotion. [registration_pipeline](registration_pipeline.py) propose the whole pipeline for the dataset registration.



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
