from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System

def main():
    win=Tk()
    app=login(win)
    win.mainloop()


class login:

    def __init__(self,root):
        self.root=root
        self.root.title("Login Page")
        self.root.geometry("1550x800+0+0")

        self.var_txtuser=StringVar()
        self.var_txtpass=StringVar()

        self.photoimg=ImageTk.PhotoImage(file=r"Images\login.jpg")
        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"Images/avatarLogin.jpg")
        img1=img1.resize((100,100))
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(image=self.photoimg1)
        f_lbl.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        User_label=Label(frame,text="Username",font=("times new roman",12,"bold"),fg="white",bg="black")
        User_label.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)
        

        password=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        # icon image 
        img2=Image.open(r"Images/avatarLogin.jpg")
        img2=img2.resize((25,25))
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(image=self.photoimg2,bg="black",borderwidth=0)
        f_lbl.place(x=650,y=323,width=25,height=25)

        img3=Image.open(r"Images/pass.png")
        img3=img3.resize((25,25))
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(image=self.photoimg3,bg="black",borderwidth=0)
        f_lbl.place(x=650,y=394,width=25,height=25)

        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="darkgreen",activebackground="darkgreen",activeforeground="white")
        loginbtn.place(x=110,y=300,width=120,height=35)

        registerbtn=Button(frame,text="New User register",command=self.register_window,font=("times new roman",15,"bold"),borderwidth=0,fg="white",bg="black",activebackground="black",activeforeground="white")
        registerbtn.place(x=20,y=350,width=160)

        Fpassbtn=Button(frame,text="Forgot Password",command=self.forgot_password_window,font=("times new roman",15,"bold"),borderwidth=0,fg="white",bg="black",activebackground="black",activeforeground="white")
        Fpassbtn.place(x=10,y=390,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all fields required")
        else:
            conn=mysql.connector.connect(host="localhost",port=3306,username="root",password="Lovedeep@1",database="registeration")
            my_cursor=conn.cursor()
            qury1=("select * from register where email=%s and pass=%s")
            vlue1=(self.txtuser.get(),self.txtpass.get(),)
            my_cursor.execute(qury1,vlue1)
            
            row=my_cursor.fetchone()
            if row==None:
               messagebox.showerror("Error","Invalid username and password")
            else:
                open_main=messagebox.askyesno("Yesno","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                    
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
    

# ================================RESET PASSWOR FUNCTION AND BELOW ALL CODE ============================
    def reset_pass(self):
        if self.combo_security_q.get()=="Select":
            messagebox.showerror("Error","Please select security question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("error","Please enter security answer",parent=self.root2)
        elif self.txt_new_pass.get()=="":
            messagebox.showerror("Error","Please enter new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",port=3306,username="root",password="Lovedeep@1",database="registeration")
            my_cursor=conn.cursor()
            qury=("select * from register where email=%s and securityQ=%s and securityA=%s")
            vlue=(self.txtuser.get(),self.combo_security_q.get(),self.txt_security.get(),)
            my_cursor.execute(qury,vlue)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct answer",parent=self.root2)
            else:
                query=("update register set pass=%s where email=%s")
                value=(self.txt_new_pass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("sucess","Password reset successfully,please login with new password",parent=self.root2)
                self.root2.destroy()

    


    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter email to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",port=3306,username="root",password="Lovedeep@1",database="registeration")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","enter valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("345x450+610+170")

                l=Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                Secuirity_q=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
                Secuirity_q.place(x=50,y=80)
        
                self.combo_security_q=ttk.Combobox(self.root2, font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_q['values']=("Select","Your pet name","Your school name","Your birth place")
                self.combo_security_q.place(x=50,y=110,width=250)
                self.combo_security_q.current(0)
        
                security_a=Label(self.root2,text="Security answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_a.place(x=50,y=150)
        
                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security.place(x=50,y=180,width=250)

                new_pass=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_pass.place(x=50,y=220)
        
                self.txt_new_pass=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_new_pass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),bg="red",fg="white")
                btn.place(x=100,y=290)




            



class Register:

    def __init__(self,root):
        self.root=root
        self.root.title("Register Page")
        self.root.geometry("1530x790+0+0")

        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_cnfpass=StringVar()
        self.var_check=IntVar()

        self.photoimg1=ImageTk.PhotoImage(file=r"Images\login.jpg")
        bg_img=Label(self.root,image=self.photoimg1)
        bg_img.place(x=0,y=0,relwidth=1,relheight=1)
        
        self.bg1=ImageTk.PhotoImage(file=r"Images\register.jpg")
        left_img=Label(self.root,image=self.bg1)
        left_img.place(x=50,y=100,width=470,height=550)

        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=880,height=550)

        reg_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        reg_lbl.place(x=20,y=20)

        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)
        
        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15))
        self.fname_entry.place(x=50,y=130,width=250)
        


        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        lname.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        contact=Label(frame,text="Contact",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

        Secuirity_q=Label(frame,text="Security question",font=("times new roman",15,"bold"),bg="white",fg="black")
        Secuirity_q.place(x=50,y=240)

        self.combo_security_q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_q['values']=("Select","Your pet name","Your school name","Your birth place")
        self.combo_security_q.current(0)
        self.combo_security_q.place(x=50,y=270,width=250)
        

        security_a=Label(frame,text="Security answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_a.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)

        

        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_email.place(x=50,y=340,width=310)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_cnfpass,font=("times new roman",15))
        self.txt_email.place(x=370,y=340,width=250)


        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree To The Terms & Conditions",font=("times new roman",15,"bold"),onvalue=1,offvalue=0,bg="white")
        checkbtn.place(x=50,y=380)

        # button 
        img=Image.open(r"Images/register1.jpg")
        img=img.resize((200,80))
        self.photoimg=ImageTk.PhotoImage(img)

        b1=Button(frame,image=self.photoimg,command=self.register_data,borderwidth=0,cursor="hand2",bg='white')
        b1.place(x=10,y=420,width=300)
        
         
        img2=Image.open(r"Images/loginImage.jpg")
        img2=img2.resize((200,100))
        self.photoimg2=ImageTk.PhotoImage(img2)

        b2=Button(frame,image=self.photoimg2,command=self.return_login,borderwidth=0,cursor="hand2",bg="white")
        b2.place(x=330,y=420,width=300)
        
    
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","all fiels are required")
        elif self.var_pass.get()!=self.var_cnfpass.get():
            messagebox("Error","Password and confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree the terms and condition")
        else:
            conn=mysql.connector.connect(host="localhost",port=3306,username="root",password="Lovedeep@1",database="registeration")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","user already exist,try another email")
            else:
                my_cursor.execute("insert into register values (%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                   
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()
                                                                                     ))
            conn.commit()
            conn.close()
            messagebox.showinfo("success","welcome")

    def return_login(self):
        self.root.destroy()
               


    


        



if __name__=="__main__":
    main()
 