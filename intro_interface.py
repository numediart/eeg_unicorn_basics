import time
import tkinter 

from playsound import playsound


# Main Window
m = tkinter.Tk()
m.title("random page")
m.geometry('720x420')
tkinter.Label(m, text="Experiment Begin", fg="red", font=('Helvetica 28')).pack(pady=150)
m.after(15000, lambda:m.destroy())
m.mainloop()

# Video 1
vidPath = 'example_vids/example.mp4'
m = tkinter.Tk()
m.title("random page")
m.geometry('720x420')
tkinter.Label(m, text="Video 1", fg="blue", font=('Helvetica 28')).pack(pady=150)
m.after(5000, lambda:m.destroy())
m.mainloop()
playsound(vidPath)