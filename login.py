from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import os
import customtkinter
from CTkMessagebox import CTkMessagebox
# --------------------------
# from register import Register
# from train import Train
# from student import Student
# from train import Train
# from face_recognition import Face_Recognition
# from attendance import Attendance
# from developer import Developer
# from helpsupport import Helpsupport



customtkinter.set_appearance_mode("dark") 
customtkinter.set_default_color_theme("dark-blue") 


def login_win():
        log=customtkinter.CTk()    
        log.title("Login page")
        log.geometry("1550x800")

        img1= customtkinter.CTkImage(light_image=Image.open("Images_GUI\\bg.jpg"),
                dark_image=Image.open("Images_GUI\\bg.jpg"),size=(1550,800))
        lbl1=customtkinter.CTkLabel(log,text="",image=img1)
        lbl1.place(x=0,y=0,relwidth=1,relheight=1)

        frame1=customtkinter.CTkFrame(log,width=460,height=580,corner_radius=0,fg_color="black")
        frame1.place(x=300,y=51)

        img= customtkinter.CTkImage(light_image=Image.open("Images_GUI\\cppname.png"),
                dark_image=Image.open("Images_GUI\\cppname.png"),size=(460,580))
        lbl=customtkinter.CTkLabel(frame1,text="",image=img)
        lbl.pack(padx=0,pady=0)

        frame=customtkinter.CTkFrame(master=log,width=460,height=580,corner_radius=0,fg_color="black")
        frame.place(x=760,y=51)#frame.pack(padx=50,pady=50)"C:\Users\shrav\Downloads\userimg.jpg"

        img2= customtkinter.CTkImage(light_image=Image.open("Images_GUI\\userimg.jpg"),
                dark_image=Image.open("Images_GUI\\userimg.jpg"),size=(100,100))
        lbl2=customtkinter.CTkLabel(frame,text="",image=img2,corner_radius=0,bg_color="black")
        lbl2.place(x=165,y=2)

        str=customtkinter.CTkLabel(master=frame,text="Get Started",font=("",20),fg_color="black",
                                bg_color="black",text_color="purple")
        str.place(x=165,y=100)
        
        
        username=customtkinter.CTkLabel(master=frame,text="Username",font=("",20),fg_color="black"
                                        ,bg_color="black",text_color="purple")
        username.place(x=90,y=180)

        img3= customtkinter.CTkImage(light_image=Image.open("Images_GUI\\usericon1.jpg"),
                dark_image=Image.open("Images_GUI\\usericon1.jpg"),size=(20,20))
        lbl3=customtkinter.CTkLabel(frame,text="",image=img3,corner_radius=0,bg_color="black")
        lbl3.place(x=65,y=180)

        userentry = customtkinter.CTkEntry(master=frame,border_color="purple",fg_color="black",
                width=320,height=30,border_width=2,corner_radius=10)
        userentry.place(x=65,y=220)

        password=customtkinter.CTkLabel(master=frame,text="Password",font=("",20),
                fg_color="black",bg_color="black", text_color="purple")
        password.place(x=90,y=280)

        img4= customtkinter.CTkImage(light_image=Image.open("Images_GUI\\passicon1.jpg"),
                dark_image=Image.open("Images_GUI\\passicon1.jpg"),size=(20,20))
        lbl4=customtkinter.CTkLabel(frame,text="",image=img4,corner_radius=0,bg_color="black")#,width=20,height=20)
        lbl4.place(x=65,y=280)

        passentry = customtkinter.CTkEntry(master=frame, border_color="purple",fg_color="black",
                width=320,height=30,border_width=2,corner_radius=10,show="*")
        passentry.place(x=65,y=320)

        def go_to_main():
                import main
                main.main_win()
                log.mainloop()


        def login_data():
                if userentry.get()=="" or passentry.get()=="":
                        CTkMessagebox(master=frame,title="Error",message="Please enter username and password!",font=("",20),fg_color="black",
                                bg_color="black",text_color="purple",button_color="purple",button_hover_color="purple",icon="cancel",
                                title_color="purple",cancel_button_color="purple",border_color="purple",button_text_color="black")
                        
                elif userentry.get()=="JJK" and passentry.get()=="1997":
                        CTkMessagebox(master=frame,title="Success",message="Login successful!",font=("",20),fg_color="black",
                                bg_color="black",text_color="purple",button_color="purple",button_hover_color="purple",button_text_color="black",
                                title_color="purple",cancel_button_color="purple",border_color="purple",icon="check") 
                        go_to_main()
                        
                        
                else:
                        
                        conn=mysql.connector.connect(host="localhost",user="root",password="Shra@2807",database="cpp")#host="localhost",user="self",password="Shra@2807",database="mydata"
                        my_cursor=conn.cursor()
                        my_cursor.execute("select * from register where enroll=%s and pwd=%s",
                                           (userentry.get(),passentry.get()))
                        row=my_cursor.fetchone()
                        if row !=None:
                                CTkMessagebox(master=frame,title="Error",message="Invalid username and password.",font=("",20),fg_color="black",
                                        bg_color="black",text_color="purple",button_color="purple",button_hover_color="purple",button_text_color="black",
                                        title_color="purple",cancel_button_color="purple",border_color="purple",icon="cancel")
                                
                        else:
                                go_to_main()
                                CTkMessagebox(master=frame,title="Info",message="Welcome to Smart Attendence Management System",font=("",20),fg_color="black",
                                        bg_color="black",text_color="purple",button_color="purple",button_hover_color="purple",button_text_color="black",
                                        title_color="purple",cancel_button_color="purple",border_color="purple",icon="info")
                                
                                # if open_main>0:
                                
                                
                                
                        conn.commit()
                        conn.close()
                        
                                
                        #CTkMessagebox(frame,title="Error",message="Invalid username and password",font=("",20),fg_color="black",
                                # bg_color="black",text_color="purple",button_color="purple",button_hover_color="purple",button_text_color="black",
                                # title_color="purple",cancel_button_color="purple",border_color="purple")

        submitbtn = customtkinter.CTkButton(master=frame, text="Submit",text_color="black",font=("",20),command=login_data,
                                fg_color="purple",hover_color="purple",
                height=30,width=320,corner_radius=10) 
        submitbtn.place(x=70,y=400)

        str2=customtkinter.CTkLabel(master=frame,text="New user?",font=("",20),fg_color="black",bg_color="black",
                                text_color="purple")
        str2.place(x=40,y=480)

       
        def register_page():
                log.destroy()
                import register
                register_page_open=customtkinter.CTkToplevel(register.register_win)

        registerbtn = customtkinter.CTkButton(master=frame, text="Register",text_color="purple",font=("",20),
                                        bg_color="Black",fg_color="black",hover_color="black",command=register_page,
                height=30,width=60,corner_radius=10) 
        registerbtn.place(x=136,y=480)
        
        def forgot_pwd():
                if userentry.get()=="" :
                        CTkMessagebox(master=frame,title="Error",message="Please enter the username to reset password",font=("",20),fg_color="black",
                                        bg_color="black",text_color="purple",button_color="purple",button_hover_color="purple",button_text_color="black",
                                        title_color="purple",cancel_button_color="purple",border_color="purple")
                else:
                        conn=mysql.connector.connect(host="localhost",user="root",password="Shra@2807",database="cpp")#host="localhost",user="self",password="Shra@2807",database="mydata"
                        my_cursor=conn.cursor()
                        query=("select * from register where email=%s ")
                        value=(userentry.get(),)
                        my_cursor.execute(query,value)
                        row=my_cursor.fetchone()
                        #print(row)
                        if row ==None:
                                CTkMessagebox(master=frame,title="Error",message="Invalid username .Please enter valid username.",font=("",20),fg_color="black",
                                        bg_color="black",text_color="purple",button_color="purple",button_hover_color="purple",button_text_color="black",
                                        title_color="purple",cancel_button_color="purple",border_color="purple")
                        else:
                                conn.close()
                                pwd=customtkinter.CTk()    
                                pwd.title("Reset Password")
                                pwd.geometry("400x500")

                                pwdframe=customtkinter.CTkFrame(master=pwd,width=400,height=500,corner_radius=0,fg_color="black")
                                pwdframe.place(x=0,y=0)
                                #Helvetica
                                str=customtkinter.CTkLabel(master=pwd,text="------Reset Password------",font=("",35),fg_color="black",bg_color="black",
                                                text_color="purple")
                                str.place(x=0,y=5)

                                username=customtkinter.CTkLabel(master=pwdframe,text="Username",font=("",20),fg_color="black"
                                                                        ,bg_color="black",text_color="purple")
                                username.place(x=30,y=100)
                                usernameentry = customtkinter.CTkEntry(master=pwdframe,border_color="purple",fg_color="black",
                                        width=320,height=30,border_width=2,corner_radius=10)
                                usernameentry.place(x=30,y=130)

                                password=customtkinter.CTkLabel(master=pwdframe,text="Password",font=("",20),
                                        fg_color="black",bg_color="black", text_color="purple")
                                password.place(x=30,y=180)
                                pwdentry = customtkinter.CTkEntry(master=pwdframe, border_color="purple",fg_color="black",
                                        width=320,height=30,border_width=2,corner_radius=10,show="*")
                                pwdentry.place(x=30,y=210)

                                confirmpassword=customtkinter.CTkLabel(master=pwdframe,text="Confirm Password",font=("",20),
                                        fg_color="black",bg_color="black", text_color="purple")
                                confirmpassword.place(x=30,y=260)
                                confirmpassentry = customtkinter.CTkEntry(master=pwdframe, border_color="purple",fg_color="black",
                                        width=320,height=30,border_width=2,corner_radius=10,show="*")
                                confirmpassentry.place(x=30,y=290)

                                def reset_data():
                                        if usernameentry.get()=="" :
                                                CTkMessagebox(master=pwdframe,title="Error",message="Please enter the username ",font=("",20),fg_color="black",
                                                        bg_color="black",text_color="purple",button_color="purple",button_hover_color="purple",button_text_color="black",
                                                        title_color="purple",cancel_button_color="purple",border_color="purple")
                                        elif pwdentry.get()=="" or confirmpassentry.get()=="":
                                                CTkMessagebox(master=pwdframe,title="Error",message="Please enter the password and confirm password fields. ",font=("",20),fg_color="black",
                                                        bg_color="black",text_color="purple",button_color="purple",button_hover_color="purple",button_text_color="black",
                                                        title_color="purple",cancel_button_color="purple",border_color="purple")
                                        else:
                                                conn=mysql.connector.connect(host="localhost",user="root",password="Shra@2807",database="cpp")#host="localhost",user="self",password="Shra@2807",database="mydata"
                                                my_cursor=conn.cursor()
                                                query=("select * from  register where email=%s ")
                                                value=(usernameentry.get(),)
                                                my_cursor.execute(query,value)
                                                row=my_cursor.fetchone()
                                                #print(row)
                                                if row ==None:
                                                        CTkMessagebox(master=pwdframe,title="Error",message="Invalid username .Please enter valid username.",font=("",20),fg_color="black",
                                                                bg_color="black",text_color="purple",button_color="purple",button_hover_color="purple",button_text_color="black",
                                                                title_color="purple",cancel_button_color="purple",border_color="purple")
                                                elif pwdentry.get()!= confirmpassentry.get():
                                                                CTkMessagebox(master=pwdframe,title="Error",message="Password and Confirm Password should be same",font=("",20),fg_color="black",
                                                                bg_color="black",text_color="purple",button_color="purple",button_hover_color="purple",button_text_color="black",
                                                                title_color="purple",cancel_button_color="purple",border_color="purple")
                                                else:
                                                        query=("update register set pwd=%s where enroll=%s ")
                                                        value=(passentry.get(),usernameentry.get())
                                                        my_cursor.execute(query,value)
                                                        
                                                        conn.commit()
                                                        conn.close()
                                                        CTkMessagebox(master=pwdframe,title="Error",message="Your password has been reset.Please login with new password ",font=("",20),fg_color="black",
                                                                bg_color="black",text_color="purple",button_color="purple",button_hover_color="purple",button_text_color="black",
                                                                title_color="purple",cancel_button_color="purple",border_color="purple")
                                                        pwd.destroy()
                                                
                                resetbtn = customtkinter.CTkButton(master=pwdframe, text="Reset",text_color="black",font=("",20),
                                                command=reset_data,fg_color="purple",hover_color="purple",
                                                height=30,width=320,corner_radius=10) 
                                resetbtn.place(x=30,y=400)

                                pwd.mainloop()
                                
                                
                        

        forgotpassbtn = customtkinter.CTkButton(master=frame, text="Forgot password",text_color="purple",font=("",20),
                                                bg_color="Black",fg_color="black",hover_color="black",
                                                command=forgot_pwd,height=30,width=60,corner_radius=10) 
        forgotpassbtn.place(x=265,y=480)

        log.mainloop()



login_win()
