from tkinter import*
import tkinter
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import  os
from train import Train
from face_reconize import Face_recognize
from attendance import Attendance
from time import strftime
from datetime import datetime

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        img=Image.open(r"C:\Users\Ramandeep\Desktop\FACE RECOGNITION SYSTEM\Images\university_image.jpg")
        img=img.resize((500,200))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=550,height=200)

        img2=Image.open(r"C:\Users\Ramandeep\Desktop\FACE RECOGNITION SYSTEM\Images\Facial-Recognition-scaled.jpg")
        img2=img2.resize((500,200))
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=500,height=200)

        #second image
        img3=Image.open(r"C:\Users\Ramandeep\Desktop\FACE RECOGNITION SYSTEM\Images\university_image.jpg")
        img3=img3.resize((500,200))
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1000,y=0,width=500,height=200)
        
        #background image
        img4=Image.open(r"C:\Users\Ramandeep\Desktop\FACE RECOGNITION SYSTEM\Images\milky-way.jpg")
        img4=img4.resize((1500,710))
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=200,width=1500,height=710)
        
        #title
        title_lbl=Label(bg_img,text="FACE RECOGNITION SYSTEM",font=("times new roman",30,"bold"),bg="red",fg="white")
        title_lbl.place(x=0,y=0,width=1500,height=40)

        #to show time on main window
        def time():
            string=strftime('%H.%M.%S %p')
            lbl.config(text=string)
            lbl.after(100,time)

        lbl=Label(title_lbl,font=('times new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=(-15),width=110,height=50)
        time()

        #button for student
        img5=Image.open(r"C:\Users\Ramandeep\Desktop\FACE RECOGNITION SYSTEM\Images\download.jpeg")
        img5=img5.resize((200,200))
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,command=self.S_details)
        b1.place(x=200,y=60,width=200,height=200)

        b1_1=Button(bg_img,text="Student_Detail",command=self.S_details)
        b1_1.place(x=200,y=260,width=200,height=40)

        
        #face detector button
        img6=Image.open(r"C:\Users\Ramandeep\Desktop\FACE RECOGNITION SYSTEM\Images\Facial-Recognition-scaled.jpg")
        img6=img6.resize((200,200))
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,command=self.face_data)
        b1.place(x=600,y=60,width=200,height=200)

        b1_1=Button(bg_img,text="Face Detector",command=self.face_data)
        b1_1.place(x=600,y=260,width=200,height=40)

        #attendanc button
        img7=Image.open(r"C:\Users\Ramandeep\Desktop\FACE RECOGNITION SYSTEM\Images\attendance.jpeg")
        img7=img7.resize((200,200))
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg5,command=self.attendance_data)
        b1.place(x=1000,y=60,width=200,height=200)

        b1_2=Button(bg_img,text="Attendance",command=self.attendance_data)
        b1_2.place(x=1000,y=260,width=200,height=40)

        #data training button
        img8=Image.open(r"C:\Users\Ramandeep\Desktop\FACE RECOGNITION SYSTEM\Images\download1.png")
        img8=img8.resize((200,200))
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,command=self.train_data)
        b1.place(x=200,y=340,width=200,height=200)

        b1_3=Button(bg_img,text="Train Data",command=self.train_data)
        b1_3.place(x=200,y=540,width=200,height=40)

        #photo button
        img9=Image.open(r"C:\Users\Ramandeep\Desktop\FACE RECOGNITION SYSTEM\Images\photos.jpeg")
        img9=img9.resize((200,200))
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,command=self.open_img)
        b1.place(x=600,y=340,width=200,height=200)

        b1_4=Button(bg_img,text="Photos",command=self.open_img)
        b1_4.place(x=600,y=540,width=200,height=40)

        #Exit face button
        img10=Image.open(r"C:\Users\Ramandeep\Desktop\FACE RECOGNITION SYSTEM\Images\exit.jpg")
        img10=img10.resize((200,200))
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,command=self.exit_here)
        b1.place(x=1000,y=340,width=200,height=200)

        b1_4=Button(bg_img,text="Exit",command=self.exit_here)
        b1_4.place(x=1000,y=540,width=200,height=40)


    def open_img(self):
        os.startfile("data")

    def exit_here(self):
        self.exit_here=tkinter.messagebox.askyesno("Face Recognition","are you sure to exit")
        if self.exit_here>0:
            self.root.destroy()
        else:
            return


      

    def S_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognize(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)










if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()     
