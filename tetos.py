from tkinter import *

from gtts import gTTS

from playsound import playsound

def tetos():

    message = text_field.get()

    speech = gTTS(text = message)

    speech.save("data.mp3")

    playsound("data.mp3")

def exit():

    window.destroy()

def reset():
    
    msg.set("")

window = Tk()

window.geometry("350x300")

window.configure(bg='#7ad7a0')

window.title("Tetos")

Label(window, text = "   Tetos    ",  font = " arial 20 bold ", bg = 'black', fg = "white").pack()

msg = StringVar()

Label(window, text = " Enter your text here : ", font = ' arial 20 bold ', fg = "darkgreen").place(x=5, y=60)

text_field = Entry(window, textvariable = msg, width = '30', font = ' arial 15 bold ', bg = "lightgreen")

text_field.place(x=5, y=100)

Button(window, text = "Next", font = 'arial 15 bold', command = tetos, width = '20', bg = 'orchid', fg = "white").place(x=35, y=140)

Button(window, font = 'arial 15 bold', text = 'Reset', width = '20', command = reset, bg = 'darkgreen', fg = "white").place(x=35, y=190)

Button(window, font = 'arail 15 bold', text = 'exit', width = '20', command = exit, bg = 'red', fg = "white").place(x=35, y=240)

window.mainloop()

