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

import cv2
import glob
import tkinter 
import datetime

import numpy as np

from playsound import playsound
from pylsl import StreamInlet, resolve_stream

def intro_page(duration=15000):
    m = tkinter.Tk()
    m.title("random page")
    m.geometry('720x420')
    tkinter.Label(m, text="Experiment Begin", fg="red", font=('Helvetica 28')).pack(pady=150)
    m.after(duration, lambda:m.destroy())
    m.mainloop()

def play_vid(vid_path, vid_id=0, duration=5000):
    m = tkinter.Tk()
    m.title("random page")
    m.geometry('720x420')
    tkinter.Label(m, text="Video "+str(vid_id), fg="blue", font=('Helvetica 28')).pack(pady=150)
    m.after(duration, lambda:m.destroy())
    m.mainloop()
    playsound(vid_path, block=True)

def len_vid(path):
    data = cv2.VideoCapture(path)
    frames = data.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = int(data.get(cv2.CAP_PROP_FPS))
    return frames/fps