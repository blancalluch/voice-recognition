from PIL import ImageTk
import PIL.Image
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import scrolledtext
import recordingVoice as rv
import predictPrep as pp


class App():
    def __init__(self):
        #background
        self.window = Tk()
        self.window.title("VoiceRecognition")
        self.canvas=Canvas(self.window,height=700,width=1000)
        self.canvas.pack()

        #background image
        self.image=PIL.Image.open("../images/b.png")
        self.background_img=ImageTk.PhotoImage(self.image)
        self.background_label = Label(self.window, image=self.background_img)
        self.background_label.place(relwidth=1, relheight=1)
            
        #title
        self.lbl1 = Label(self.window, text="VoiceRecognition",fg="white",bg="black", width=200)
        self.lbl1.place(relx=0.5, rely=0.1,relwidth=0.5, relheight=0.09,anchor='n')
        self.lbl1.config(font=("Helvetica Bold", 40))

        # button - Add audio from new person
        self.frame2 = Frame(self.window, bg='black', bd=1)
        self.frame2.place(relx=0.25, rely=0.78, relwidth=0.2,
                    relheight=0.04, anchor='n')

        self.button2 = Button(self.frame2, text="Add audio from new person", font=("Helvetica Bold",12),command=self.add_audio)
        self.button2.place(relx=0, relheight=1, relwidth=1)
        self.button2.configure(foreground='white',bg='black',relief='solid')

        #gender selection
        self.lbl2 = Label(self.window, text="Gender:",font=("Helvetica", 12))
        self.lbl2.place(relx=0.385, rely=0.78,relwidth=0.045,
                    relheight=0.04, anchor='n')

        self.combo = Combobox(self.window)
        self.combo['values']= ('M','F')
        self.combo.place(relx=0.44, rely=0.78, relwidth=0.06,
                    relheight=0.04, anchor='n')

        #name entry
        self.lbl3 = Label(self.window, text="Name:",font=("Helvetica", 12))
        self.lbl3.place(relx=0.525, rely=0.78,relwidth=0.04,
                    relheight=0.04, anchor='n')

        self.txt1 = Entry(self.window)
        self.txt1.place(relx=0.6, rely=0.78,relwidth=0.09,
                    relheight=0.04, anchor='n')

        #surname entry
        self.lbl4 = Label(self.window, text="Surname:",font=("Helvetica", 12))
        self.lbl4.place(relx=0.68, rely=0.78,relwidth=0.07,
                    relheight=0.04, anchor='n')

        self.txt2 = Entry(self.window)
        self.txt2.place(relx=0.761, rely=0.78,relwidth=0.09,
                    relheight=0.04, anchor='n')

        # button - predict name
        frame1 = Frame(self.window, bg='black',bd=10)
        frame1.place(relx=0.5, rely=0.85, relwidth=0.7,
                    relheight=0.07, anchor='n')

        button1 = Button(frame1, bg="black", text="Predict Name", font=("Helvetica Bold",19),command=self.predict)
        button1.place(relx=0,rely=0, relheight=1, relwidth=1)
        button1.configure(foreground='white' ,fg='black',relief='solid')


    def add_audio(self):
        self.lbl5 = Label(self.window, text="Recording...",fg="white",bg="black", width=200)
        self.lbl5.place(relx=0.5, rely=0.2,relwidth=0.2, relheight=0.075,anchor='n')
        self.lbl5.config(font=("Helvetica Bold", 20))
        rv.recording(24000,1000,f'../input/{self.combo.get()}{self.txt1.get()+self.txt2.get()}.wav',0,2)

    def predict(self):
        self.lbl6 = Label(self.window, text="Predicting name...",fg="white",bg="black", width=200)
        self.lbl6.place(relx=0.5, rely=0.2,relwidth=0.2, relheight=0.075,anchor='n')
        self.lbl6.config(font=("Helvetica Bold", 20))
        res=rv.recording(24000,1000,0,1,40)
        self.scrolltxt2 = scrolledtext.ScrolledText(self.window)
        self.scrolltxt2.place(relx=0.85, rely=0.05,relwidth=0.325, relheight=0.5,anchor='n')
        self.scrolltxt2.insert(INSERT,'\n'.join([e[0] for e in res]))
        self.lbl6.config(text="Finished predicting.")


a = App()
a.window.mainloop()