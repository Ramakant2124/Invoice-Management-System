from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import os
#from dashboard import IMS
class loginclass:
    def __init__(self,root):
        self.root=root
        self.root.title("login Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#8D8C79")
        
         #=====login from=======
        login_frame=Frame(self.root,bg="lightyellow",relief=RIDGE,bd=50)
        login_frame.place(x=360,y=100,height=500,width=700)
    
         
    
        title=Label(login_frame,text="Login Here",font=("time new roman",20,"bold"),bg="#0AC5F4",fg="Black").place(x=0,y=0,width=600,height=40)
        
        
        email=Label(login_frame,text="Username :",font=("time new roman",25,"bold"),bg="lightyellow",fg="#d77337").place(x=220,y=100)
        self.txt_email=Entry(login_frame,font=("time new roman",15),bg="lightgray")
        self.txt_email.place(x=190,y=150,width=250,height=40)
        
        password=Label(login_frame,text="Password :",font=("time new roman",25,"bold"),bg="lightyellow",fg="#d77337").place(x=220,y=200)
        self.txt_password=Entry(login_frame,font=("time new roman",15),bg="lightgray",show="*")
        self.txt_password.place(x=190,y=250,width=250,height=40)
        
        btn_login=Button(login_frame,text="Login",command=self.login,font=("time new roman",15,"bold"),fg="Black",bg="#0AC5F4").place(x=200,y=340,width=200,height=50)
        
    def login(self):
        if self.txt_email.get()=='Hemant' and self.txt_password.get()=='Hemant@6429':
            self.root.destroy()
            os.system("python dashboard.py")
        elif self.txt_email.get()=='' and self.txt_password.get()=='':
            messagebox.showerror('Error',"All fields are required",parent=self.root)
        else:
            messagebox.showerror('Error',"Username or Password Incorrect",parent=self.root)

            
    
        
root=Tk()
obj=loginclass(root)
root.mainloop()