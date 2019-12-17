import tkinter as tk
from tkinter import Label, Button 
import recordingVoice as rv
 
window = tk.Tk()
window.geometry('600x450')
window.title("Sound Recognition")
window.configure(bg='light blue')

lbl1 = tk.Label(window, text="Sound Recognition",font=("Arial Underlined", 30))
lbl1.grid(column=10, row=3)
lbl1.place(x=150, y=10)

lbl2 = tk.Label(window, text="Predict Name",font=("Arial", 15))
lbl2.grid(column=10, row=3)
lbl2.place(x=100, y=150)

lbl3 = tk.Label(window, text="Add Person",font=("Arial", 15))
lbl3.grid(column=10, row=3)
lbl3.place(x=375, y=150)


lbl4 = tk.Label(window, text="Gender(H/M)",font=("Arial", 10))
lbl4.grid(column=10, row=3)
lbl4.place(x=300, y=290)

txt1 = tk.Entry(window,width=10)
txt1.grid(column=10, row=3)
txt1.place(x=375, y=275)
name='Blanca'
def clicked1():
    lbl2.configure(text="Predicting person...")
    '''updates dataset with audio from a new person'''
    '''calling function recording with rate=35000 and chunk=1000' (35 seconds)'''
    rv.recording(35000,1000,f'../input/{txt1.get()}{name}.wav',0)


def clicked2():
    lbl3.configure(text="Recording audio...")
    '''returns name of the person speaking'''
    rv.recording(24000,1000,0,1)
 
btn1 = tk.Button(window, text="Predict Name", command=clicked1,bg='blue',fg='red')
btn1.place(x=100, y=200)


btn2 = tk.Button(window, text="Add Person", command=clicked2,background="blue")
btn2.place(x=375, y=200)


 
window.mainloop()