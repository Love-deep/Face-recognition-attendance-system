from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


myData=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("ATTENDANCE")

        #variables
        self.var_attend_id=StringVar()
        self.var_attend_roll=StringVar()
        self.var_attend_name=StringVar()
        self.var_attend_dep=StringVar()
        self.var_attend_time=StringVar()
        self.var_attend_date=StringVar()
        self.var_attend_attendance=StringVar()

        img=Image.open(r"C:\Users\Ramandeep\Desktop\FACE RECOGNITION SYSTEM\Images\student1.jpg")
        img=img.resize((750,200))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=750,height=200)

        img2=Image.open(r"C:\Users\Ramandeep\Desktop\FACE RECOGNITION SYSTEM\Images\student2.jpg")
        img2=img2.resize((750,200))
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=750,y=0,width=750,height=200)

        img4=Image.open(r"C:\Users\Ramandeep\Desktop\FACE RECOGNITION SYSTEM\Images\milky-way.jpg")
        img4=img4.resize((1500,710))
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=200,width=1500,height=710)

        title_lbl=Label(bg_img,text="ATTENDANCE",font=("times new roman",30,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1500,height=40)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=48,width=1470,height=650)
        

        #left frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",22,"bold"))
        left_frame.place(x=50,y=10,width=660,height=500)

        imgl=Image.open(r"C:\Users\Ramandeep\Desktop\FACE RECOGNITION SYSTEM\Images\student2.jpg")
        imgl=imgl.resize((620,130))
        self.photoimgl=ImageTk.PhotoImage(imgl)

        f_lbl=Label(left_frame,image=self.photoimgl)
        f_lbl.place(x=20,y=0,width=630,height=120)

        course_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Current course",font=("times new roman",20,"bold"))
        course_frame.place(x=55,y=135,width=650,height=370)

    # labels and entry
        AttendaceId_label=Label(course_frame,text="Attendance_Id",font=("times new roman",12,"bold"),bg="white")
        AttendaceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        # attendance id
        AttendaceId_entry=ttk.Entry(course_frame,width=20,textvariable=self.var_attend_id,font=("times new roman",12,"bold"))
        AttendaceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        # Rollno
        Roll_label=Label(course_frame,text="Roll:",font=("times new roman",12,"bold"),bg="white")
        Roll_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        Roll_entry=ttk.Entry(course_frame,width=20,textvariable=self.var_attend_roll,font=("times new roman",12,"bold"))
        Roll_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        #name
        Name_label=Label(course_frame,text="Name:",font=("times new roman",12,"bold"),bg="white")
        Name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)  
        Name_entry=ttk.Entry(course_frame,width=20,textvariable=self.var_attend_name,font=("times new roman",12,"bold"))
        Name_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        #department
        Dep_label=Label(course_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        Dep_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        Dep_entry=ttk.Entry(course_frame,width=20,textvariable=self.var_attend_dep,font=("times new roman",12,"bold"))
        Dep_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        #time
        time_label=Label(course_frame,text="Time:",font=("times new roman",12,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        time_entry=ttk.Entry(course_frame,width=20,textvariable=self.var_attend_time,font=("times new roman",12,"bold"))
        time_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        #date
        date_label=Label(course_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
        date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        date_entry=ttk.Entry(course_frame,width=20,textvariable=self.var_attend_date,font=("times new roman",12,"bold"))
        date_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        #attendance
        atten_label=Label(course_frame,text="Attendance:",font=("times new roman",12,"bold"),bg="white")
        atten_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        attend_combo=ttk.Combobox(course_frame,textvariable=self.var_attend_attendance,font=("times new roman",12,"bold"),state="readonly")
        attend_combo["values"]=("Status","Present","Absent")
        attend_combo.current(0)
        attend_combo.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        # button frame 
        btn_frame=Frame(course_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=250,width=650,height=35)

        save_btn=Button(btn_frame,text="Import csv",command=self.importcsv,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=6,column=0)

        update_btn=Button(btn_frame,text="Export csv",command=self.exportcsv,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=6,column=1)

        delete_btn=Button(btn_frame,text="Update",width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=6,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=6,column=3)



        


        



        # right frame 
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",20,"bold"))
        right_frame.place(x=750,y=10,width=660,height=500)

        table_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=5,width=640,height=450)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendace ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        
        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)


        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    #import csv function button
    def importcsv(self):
        global myData
        myData.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                myData.append(i)
            self.fetchData(myData)
    #import csv function button
    def exportcsv(self):
        try:
            if len(myData)<1:
                messagebox.showerror("No Data","NO Data found to Export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="\n") as myfile:
                export_write=csv.writer(myfile,delimiter=",")
                for i in myData:
                    export_write.writerow(i)
                messagebox.showinfo("Data export","Your Data exported to"+os.path.basename(fln)+"Successfull")
        except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root) 

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_attend_id.set(rows[0])
        self.var_attend_roll.set(rows[1])
        self.var_attend_name.set(rows[2])
        self.var_attend_dep.set(rows[3])
        self.var_attend_time.set(rows[4])
        self.var_attend_date.set(rows[5])
        self.var_attend_attendance.set(rows[6])

    def reset_data(self):
        self.var_attend_id.set("")
        self.var_attend_roll.set("")
        self.var_attend_name.set("")
        self.var_attend_dep.set("")
        self.var_attend_time.set("")
        self.var_attend_date.set("")
        self.var_attend_attendance.set("")




    


        









if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()     
