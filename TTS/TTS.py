from tkinter import *
from gtts import gTTS
from playsound import playsound
import os 
from PIL import Image, ImageTk

path = os.path.abspath('tf2.png')

gui = Tk()
gui.geometry("350x200")
gui.resizable(0,0)
gui.title("Text To Speech")
gui.configure(bg='white smoke')


Label(gui, text = "Text To Speech", font = "arial 20 bold", bg = 'white smoke').pack()

Msg = StringVar()
Label(gui, text = "Enter Text", font = 'arial 15 bold', bg = 'white smoke').place(x = 20 , y = 60)

entry_field = Entry(gui, textvariable = Msg , width = '50')
entry_field.place(x = 20 , y = 100)

def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('TTS.mp3')
    playsound('TTS.mp3')
    os.remove("TTS.mp3")

def Reset():
    Msg.set("")

img = ImageTk.PhotoImage(Image.open(path))
gui.iconphoto(False, img)

Button(gui, text = "PLAY", font = 'arial 15 bold' , command = Text_to_speech ,width = '4').place(x = 25 , y = 140)
Button(gui, font = 'arial 15 bold',text = 'RESET', width = '6' , command = Reset).place(x=100 , y = 140)

gui.mainloop()