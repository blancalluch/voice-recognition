from PIL import ImageTk
import PIL.Image
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import scrolledtext
import recordingVoice as rv

#background
window = Tk()
window.title("VoiceRecognition")
canvas=Canvas(window,height=700,width=1000)
canvas.pack()

#background image
image=PIL.Image.open("../images/b.png")
background_img=ImageTk.PhotoImage(image)
background_label = Label(window, image=background_img)
background_label.place(relwidth=1, relheight=1)
    
#title
lbl1 = Label(window, text="VoiceRecognition",fg="white",bg="black", width=200)
lbl1.place(relx=0.5, rely=0.1,relwidth=0.5, relheight=0.09,anchor='n')
lbl1.config(font=("Helvetica Bold", 40))

def clicked1():
    #lbl2.configure(text="Predicting person...")
    #returns name of the person speaking
    rv.recording(24000,1000,0,1)
    #txt3.insert(tk.INSERT,f'TOP:{topName} [{otherNames}]')

def clicked2():
    #lbl3.configure(text="Recording audio...")
    #updates dataset with audio from a new person
    #calling function recording with rate=35000 and chunk=1000' (35 seconds)
    rv.recording(35000,1000,f'../input/{combo.get()}{txt1.get()+txt2.get()}.wav',0)

# button - Add audio from new person
frame2 = Frame(window, bg='black', bd=1)
frame2.place(relx=0.25, rely=0.78, relwidth=0.2,
            relheight=0.04, anchor='n')

button2 = Button(frame2, text="Add audio from new person", font=("Helvetica Bold",12),command=clicked2())
button2.place(relx=0, relheight=1, relwidth=1)
button2.configure(foreground='white',bg='black',relief='solid')

lbl2 = Label(window, text="Gender:",font=("Helvetica", 12))
lbl2.place(relx=0.385, rely=0.78,relwidth=0.045,
            relheight=0.04, anchor='n')

combo = Combobox(window)
combo['values']= ('M','H')
combo.place(relx=0.44, rely=0.78, relwidth=0.06,
            relheight=0.04, anchor='n')

lbl3 = Label(window, text="Name:",font=("Helvetica", 12))
lbl3.place(relx=0.525, rely=0.78,relwidth=0.04,
            relheight=0.04, anchor='n')

txt1 = Entry(window)
txt1.place(relx=0.6, rely=0.78,relwidth=0.09,
            relheight=0.04, anchor='n')

lbl4 = Label(window, text="Surname:",font=("Helvetica", 12))
lbl4.place(relx=0.68, rely=0.78,relwidth=0.07,
            relheight=0.04, anchor='n')

txt2 = Entry(window)
txt2.place(relx=0.761, rely=0.78,relwidth=0.09,
            relheight=0.04, anchor='n')

# button - predict name
frame1 = Frame(window, bg='black',bd=10)
frame1.place(relx=0.5, rely=0.85, relwidth=0.7,
            relheight=0.07, anchor='n')

button1 = Button(frame1, bg="black", text="Predict Name", font=("Helvetica Bold",19),command=clicked1())
button1.place(relx=0,rely=0, relheight=1, relwidth=1)
button1.configure(foreground='white' ,fg='black',relief='solid')

#result text
'''canvas2=Canvas(window,height=200,width=200)
canvas2.pack()
canvas2.place(relx=0, rely=0,relwidth=1, relheight=1,anchor='n')
background_label = Label(canvas2, image=background_img)
background_label.place(relwidth=1, relheight=1)'''

#txt = scrolledtext.ScrolledText(window)
#txt.place(relx=0.85, rely=0.05,relwidth=0.325, relheight=0.5,anchor='n')
#txt.insert(INSERT,'result')
#background_label = Label(txt, image=background_img)
#ibackground_label.place(relwidth=1, relheight=1)

window.mainloop()