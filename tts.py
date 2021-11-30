import tkinter as tk
import pyttsx3

engine = pyttsx3.init()

root = tk.Tk()
root.title('Text-To-Speach')
root.configure(background="pink")

lable = tk.Label(root,text="Type here something",font="arial 25 bold",bg="pink",fg="blue")
lable.pack()

textbox = tk.Entry(root,width=30,font="arial 20",bg="grey")
textbox.pack()

def speak(text):
    engine.say(text)
    engine.runAndWait()

button = tk.Button(root,text="SPEAK",font="arial 25 bold",bg="yellow",fg="blue",command=lambda:speak(textbox.get()))
button.pack()

root.mainloop()
