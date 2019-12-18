import tkinter as tk
from tkinter import Label, Button 
import recordingVoice as rv
from tkinter import scrolledtext
from tkinter import messagebox
 
window = tk.Tk()
window.geometry('700x550')
window.title("Sound Recognition")
window.configure(bg='light blue')

lbl1 = tk.Label(window, text="Sound Recognition",font=("Arial Underlined", 30))
lbl1.grid(column=10, row=3)
lbl1.place(x=300, y=10)

lbl2 = tk.Label(window, text="Predict Name",font=("Arial", 20))
lbl2.grid(column=10, row=3)
lbl2.place(x=100, y=70)

lbl3 = tk.Label(window, text="Add Person",font=("Arial", 20))
lbl3.grid(column=10, row=3)
lbl3.place(x=505, y=70)

lbl4 = tk.Label(window, text="Gender(H/M)",font=("Arial", 15))
lbl4.grid(column=10, row=3)
lbl4.place(x=395, y=225)

txt1 = tk.Entry(window,width=10)
txt1.grid(column=10, row=3)
txt1.place(x=505, y=220)

lbl5 = tk.Label(window, text="NameSurname",font=("Arial", 15))
lbl5.grid(column=10, row=3)
lbl5.place(x=395, y=295)

txt2 = tk.Entry(window,width=10)
txt2.grid(column=10, row=3)
txt2.place(x=505, y=290)

def clicked1():
    lbl2.configure(text="Predicting person...")
    '''updates dataset with audio from a new person'''
    '''calling function recording with rate=35000 and chunk=1000' (35 seconds)'''
    rv.recording(35000,1000,f'../input/{txt1.get()}{txt2.get()}.wav',0)


def clicked2():
    lbl3.configure(text="Recording audio...")
    '''returns name of the person speaking'''
    rv.recording(24000,1000,0,1)
 
btn1 = tk.Button(window, text="Predict Name", command=clicked2,bg='blue',fg='red')
btn1.place(x=100, y=120)


btn2 = tk.Button(window, text="Add Person", command=clicked1,background="blue")
btn2.place(x=505, y=120)

txt3 = scrolledtext.ScrolledText(window,width=50,height=23)
txt3.grid(column=0,row=0)
txt3.place(x=20,y=172)
txt3.insert(tk.INSERT,'You text goes here')

 
window.mainloop()