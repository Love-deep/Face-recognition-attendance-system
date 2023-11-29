from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np



class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")


        title_lbl=Label(self.root,text="Training Data",font=("times new roman",30,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1500,height=40)


        img=Image.open(r"C:\Users\Ramandeep\Desktop\FACE RECOGNITION SYSTEM\Images\Facial-Recognition-scaled.jpg")
        img=img.resize((1500,300))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=55,width=1500,height=300)

        b1=Button(self.root,text="TRAIN DATA",command=self.training,cursor="hand1",font=("times new roman",25,"bold"),bg="blue",fg="white")
        b1.place(x=0,y=380,width=1500,height=60)


        img1=Image.open(r"C:\Users\Ramandeep\Desktop\FACE RECOGNITION SYSTEM\Images\Facial-Recognition-scaled.jpg")
        img1=img.resize((1500,300))
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=450,width=1500,height=300)

    def training(self):
        data_file=("data")
        path=[os.path.join(data_file,file) for file in os.listdir(data_file)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')  #gray scale img conversion
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #train classifierthen save
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets comlete.")


        












if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()     
