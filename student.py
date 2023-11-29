from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")


        #variables for entry field
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        
        

        img=Image.open(r"C:\Users\Ramandeep\Desktop\FACE RECOGNITION SYSTEM\Images\student1.jpg")
        img=img.resize((500,200))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=550,height=200)

        img2=Image.open(r"C:\Users\Ramandeep\Desktop\FACE RECOGNITION SYSTEM\Images\student2.jpg")
        img2=img2.resize((500,200))
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=500,height=200)

        #second image
        img3=Image.open(r"C:\Users\Ramandeep\Desktop\FACE RECOGNITION SYSTEM\Images\student3.jpg")
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
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1500,height=40)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=48,width=1470,height=650)

        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",22,"bold"))
        left_frame.place(x=50,y=10,width=660,height=500)

        imgl=Image.open(r"C:\Users\Ramandeep\Desktop\FACE RECOGNITION SYSTEM\Images\student2.jpg")
        imgl=imgl.resize((620,120))
        self.photoimgl=ImageTk.PhotoImage(imgl)

        f_lbl=Label(left_frame,image=self.photoimgl)
        f_lbl.place(x=20,y=0,width=630,height=120)

        #course informntion 
        course_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Current course",font=("times new roman",20,"bold"))
        course_frame.place(x=55,y=135,width=650,height=120)
        
        #department label
        dep_label=Label(course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)


        dep_combo=ttk.Combobox(course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("select department","SEDA","GBS","SOH","SCS")
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course combobox
        course_label=Label(course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10)


        course_combo=ttk.Combobox(course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly")
        course_combo["values"]=("select  course","B.Tech","BBA","BSC IT","Hotel manangement")
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
     
        #YEAR LABEL
        year_label=Label(course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10)


        year_combo=ttk.Combobox(course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly")
        year_combo["values"]=("select year","2020-21","2021-22","2022-23","2023-24")
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        sem_label=Label(course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=10)


        sem_combo=ttk.Combobox(course_frame,textvariable=self.var_sem,font=("times new roman",12,"bold"),state="readonly")
        sem_combo["values"]=("select semester","sem-1","sem-2","sem-3","sem-4")
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #student ind=formation
        Student_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("times new roman",20,"bold"))
        Student_frame.place(x=55,y=260,width=650,height=240)

        StudentId_label=Label(Student_frame,text="Student_Id",font=("times new roman",12,"bold"),bg="white")
        StudentId_label.grid(row=0,column=0,padx=10,sticky=W)

        StudentId_entry=ttk.Entry(Student_frame,textvariable=self.var_id,width=20,font=("times new roman",12,"bold"))
        StudentId_entry.grid(row=0,column=1,padx=10,sticky=W)

        #student name
        Studentname_label=Label(Student_frame,text="Student_name",font=("times new roman",12,"bold"),bg="white")
        Studentname_label.grid(row=0,column=2,padx=10,sticky=W)

        Studentname_entry=ttk.Entry(Student_frame,textvariable=self.var_name,width=20,font=("times new roman",12,"bold"))
        Studentname_entry.grid(row=0,column=3,padx=10,sticky=W)

        #student class division
        Studentdiv_label=Label(Student_frame,text="Class_division",font=("times new roman",12,"bold"),bg="white")
        Studentdiv_label.grid(row=1,column=0,padx=10,pady=3,sticky=W)

        
        Studentdiv_combo=ttk.Combobox(Student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly")
        Studentdiv_combo["values"]=("A","B","C","D","F")
        Studentdiv_combo.current(0)
        Studentdiv_combo.grid(row=1,column=1,padx=2,pady=3,sticky=W)

        #registration number
        StudentRoll_label=Label(Student_frame,text="Roll_no",font=("times new roman",12,"bold"),bg="white")
        StudentRoll_label.grid(row=1,column=2,padx=10,pady=3,sticky=W)

        StudentReg_entry=ttk.Entry(Student_frame,width=20,textvariable=self.var_roll,font=("times new roman",12,"bold"))
        StudentReg_entry.grid(row=1,column=3,padx=10,pady=3,sticky=W)

        #student gender
        Gender_label=Label(Student_frame,text="Gender",font=("times new roman",12,"bold"),bg="white")
        Gender_label.grid(row=2,column=0,padx=10,pady=3,sticky=W)

        
        Gender_combo=ttk.Combobox(Student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly")
        Gender_combo["values"]=("select gender","Male","Female","Others")
        Gender_combo.current(0)
        Gender_combo.grid(row=2,column=1,padx=2,pady=3,sticky=W)



        #DOB
        StudentDob_label=Label(Student_frame,text="DOB",font=("times new roman",12,"bold"),bg="white")
        StudentDob_label.grid(row=2,column=2,padx=10,pady=3,sticky=W)

        StudentDob_entry=ttk.Entry(Student_frame,width=20,textvariable=self.var_dob,font=("times new roman",12,"bold"))
        StudentDob_entry.grid(row=2,column=3,padx=10,pady=3,sticky=W)

        #email
        StudentEmail_label=Label(Student_frame,text="Email",font=("times new roman",12,"bold"),bg="white")
        StudentEmail_label.grid(row=3,column=0,padx=10,pady=3,sticky=W)

        StudentEmail_entry=ttk.Entry(Student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        StudentEmail_entry.grid(row=3,column=1,padx=10,pady=3,sticky=W)

        #contact
        Phone_label=Label(Student_frame,text="Phone",font=("times new roman",12,"bold"),bg="white")
        Phone_label.grid(row=3,column=2,padx=10,pady=3,sticky=W)

        Phone_entry=ttk.Entry(Student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        Phone_entry.grid(row=3,column=3,padx=10,pady=3,sticky=W)

        #address
        Address_label=Label(Student_frame,text="Address",font=("times new roman",12,"bold"),bg="white")
        Address_label.grid(row=4,column=0,padx=10,pady=3,sticky=W)

        Address_entry=ttk.Entry(Student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        Address_entry.grid(row=4,column=1,padx=10,pady=3,sticky=W)

        #teacher name
        Teacher_label=Label(Student_frame,text="Teacher_name",font=("times new roman",12,"bold"),bg="white")
        Teacher_label.grid(row=4,column=2,padx=10,pady=3,sticky=W)

        Teacher_entry=ttk.Entry(Student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        Teacher_entry.grid(row=4,column=3,padx=10,pady=3,sticky=W)


        # radio buttons
        self.var_radio1=StringVar()
        radiobutton1=ttk.Radiobutton(Student_frame,variable=self.var_radio1,text="Photo sample",value="yes")
        radiobutton1.grid(row=5,column=0)

        
        radiobutton2=ttk.Radiobutton(Student_frame,variable=self.var_radio1,text="No Photo sample",value="No")
        radiobutton2.grid(row=5,column=2)

        # button frame
        btn_frame=Frame(Student_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=168,width=630,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=9,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=6,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=9,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=6,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=9,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=6,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=9,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=6,column=3)

        takePhoto_btn=Button(btn_frame,command=self.generate_dataset,text="TakePhotoSample",width=13,font=("times new roman",12,"bold"),bg="blue",fg="white")
        takePhoto_btn.grid(row=6,column=4)

        update_btn=Button(btn_frame,text="UpdatePhotoSample",width=14,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=6,column=5)

       

        #right label
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",20,"bold"))
        right_frame.place(x=750,y=10,width=660,height=500)

        imgr=Image.open(r"C:\Users\Ramandeep\Desktop\FACE RECOGNITION SYSTEM\Images\student2.jpg")
        imgr=imgr.resize((600,90))
        self.photoimgr=ImageTk.PhotoImage(imgr)

        f_lbl=Label(right_frame,image=self.photoimgr)
        f_lbl.place(x=25,y=0,width=600,height=90)

        # search frame

        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search system",font=("times new roman",20,"bold"))
        search_frame.place(x=5,y=100,width=640,height=90)

        search_label=Label(search_frame,text="search by:",font=("times new roman",12,"bold"),bg="red")
        search_label.grid(row=0,column=0,padx=10,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",10,"bold"),state="readonly")
        search_combo["values"]=("Registration_num")
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=20,font=("times new roman",10,"bold"))
        search_entry.grid(row=0,column=2,padx=10,sticky=W)


        search_btn=Button(search_frame,text="search",width=10,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3)

        showAll_btn=Button(search_frame,text="showAll",width=10,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4)

        # table frame
        table_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=640,height=250)

        scroll_x=ttk.Scrollbar(table_frame,orient="horizontal")
        scroll_y=ttk.Scrollbar(table_frame,orient="vertical")

        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student_id")
        self.student_table.heading("name",text="studentName")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll_no")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")

      
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)
        

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        # **********************function declaration***************

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","all fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",port=3306,username="root",password="Lovedeep@1",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_dep.get(),  
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_sem.get(),
                                                                                                            self.var_id.get(),
                                                                                                            self.var_name.get(),
                                                                                                            self.var_div.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_teacher.get(),
                                                                                                            self.var_radio1.get()
                                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Sucess","Student Details has Been Added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root) 

    #fetching data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Lovedeep@1",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()   

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()



    # =============get cursor============
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_sem.set(data[3])
        self.var_id.set(data[4])
        self.var_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])

    #update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","all fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",port=3306,username="root",password="Lovedeep@1",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photosample=%s where Student_id=%s",(
                                                                                                                                                                                            
                                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                            self.var_sem.get(),
                                                                                                                                                                                            self.var_name.get(),
                                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                            self.var_teacher.get(),
                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                            self.var_id.get()
                                                                                                                                                                                        ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


    # delete function
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","student id must required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delet this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",port=3306,username="root",password="Lovedeep@1",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","successfully deleted Student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


    # reset value
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")


    # ==========Generate photo samples by taking pics =============
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","all fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",port=3306,username="root",password="Lovedeep@1",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photosample=%s where Student_id=%s",(
                                                                                                                                                                                            
                                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                            self.var_sem.get(),
                                                                                                                                                                                            self.var_name.get(),
                                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                            self.var_teacher.get(),
                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                            self.var_id.get()==id+1
                                                                                                                                                                                        ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_croped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor 1.3  minimum neihbur 5

                    for(x,y,w,h) in faces:
                        face_croped=img[y:y+h,x:x+w]
                        return face_croped
                
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_croped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_croped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Croped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                
                        break
                cap.release()
                cv2.destroyAllWindows()

                messagebox.showinfo("Result","Generating data sets completed.",parent=self.root)
            
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)





if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()     
