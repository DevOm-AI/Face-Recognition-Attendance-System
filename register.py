from tkinter import *
import customtkinter
from PIL import Image
from CTkMessagebox import CTkMessagebox
import mysql.connector


customtkinter.set_appearance_mode("dark")  
customtkinter.set_default_color_theme("dark-blue") 
 
 
#=====================================Register Window================================================

        
def register_win():
        
        root=customtkinter.CTk()      
        root.title("Registration page")
        root.geometry("1550x800")

        img1= customtkinter.CTkImage(light_image=Image.open("Images_GUI\\bg.jpg"),
                dark_image=Image.open("Images_GUI\\bg.jpg"),size=(1550,800))
        lbl1=customtkinter.CTkLabel(root,text="",image=img1)
        lbl1.place(x=0,y=0,relwidth=1,relheight=1)

        frame1=customtkinter.CTkFrame(master=root,width=360,height=680,corner_radius=0,fg_color="black")
        frame1.place(x=100,y=51)

        img= customtkinter.CTkImage(light_image=Image.open("Images_GUI\\cppname.png"),
                dark_image=Image.open("Images_GUI\\cppname.png"),size=(410,680))
        lbl=customtkinter.CTkLabel(frame1,text="",image=img)
        lbl.pack(padx=0,pady=0)

        frame=customtkinter.CTkFrame(master=root,width=860,height=680,corner_radius=0,fg_color="black")
        frame.place(x=510,y=51)

        str=customtkinter.CTkLabel(master=frame,text="Register Here!",font=("Times new roman",60,"bold"),fg_color="black",bg_color="black",
                text_color="purple")
        str.place(x=10,y=5)

        

        name=customtkinter.CTkLabel(master=frame,text="Full Name ",font=("",20),fg_color="black",
                bg_color="black",text_color="purple")
        name.place(x=30,y=120)
        nameentry = customtkinter.CTkEntry(master=frame,border_color="purple",fg_color="black",
                width=320,height=30,border_width=2,corner_radius=10)
        nameentry.place(x=30,y=150)

        enroll=customtkinter.CTkLabel(master=frame,text="Enrollment No. ",font=("",20),fg_color="black",
                bg_color="black",text_color="purple")
        enroll.place(x=500,y=120)
        enrollentry = customtkinter.CTkEntry(master=frame,border_color="purple",fg_color="black",
                width=320,height=30,border_width=2,corner_radius=10)
        enrollentry.place(x=500,y=150)

        email=customtkinter.CTkLabel(master=frame,text="Email ",font=("",20),fg_color="black",
                bg_color="black",text_color="purple")
        email.place(x=30,y=230)
        emailentry = customtkinter.CTkEntry(master=frame,border_color="purple",fg_color="black",
                width=320,height=30,border_width=2,corner_radius=10)
        emailentry.place(x=30,y=260)

        contact=customtkinter.CTkLabel(master=frame,text="Contact No. ",font=("",20),fg_color="black",
                bg_color="black",text_color="purple")
        contact.place(x=500,y=230)
        contactentry = customtkinter.CTkEntry(master=frame,border_color="purple",fg_color="black",
                width=320,height=30,border_width=2,corner_radius=10)
        contactentry.place(x=500,y=260)

        pwd=customtkinter.CTkLabel(master=frame,text="Password ",font=("",20),fg_color="black",
                bg_color="black",text_color="purple")
        pwd.place(x=30,y=330)
        pwdentry = customtkinter.CTkEntry(master=frame,border_color="purple",fg_color="black",
                width=320,height=30,border_width=2,corner_radius=10,show="*")
        pwdentry.place(x=30,y=360)

        confirmpwd=customtkinter.CTkLabel(master=frame,text="Confirm Password ",font=("",20),fg_color="black",
                bg_color="black",text_color="purple")
        confirmpwd.place(x=500,y=330)
        confirmpwdentry = customtkinter.CTkEntry(master=frame,border_color="purple",fg_color="black",
                width=320,height=30,border_width=2,corner_radius=10,show="*")
        confirmpwdentry.place(x=500,y=360)

        

        check_var= customtkinter.StringVar(value="off")
        my_check=customtkinter.CTkCheckBox(master=frame,text="I agree  to the Terms and Conditions.",font=("",20),
                bg_color="black",fg_color="black",text_color="purple",checkmark_color="purple",border_color="purple",
                variable=check_var,onvalue="ON",offvalue="OFF",hover_color="black")
        my_check.place(x=30,y=430)

        def register_data():            
                if nameentry.get()=="" or enrollentry.get()=="" or  emailentry.get()=="" or contactentry.get()=="" or pwdentry.get()==""or confirmpwdentry.get()=="" :
                        CTkMessagebox(master=frame,title="Error",message="Please fill the required fields!",font=("",20),fg_color="black",
                                bg_color="black",text_color="purple",button_color="purple",button_hover_color="purple",button_text_color="black",
                                title_color="purple",cancel_button_color="purple",border_color="purple")
                elif pwdentry.get()!= confirmpwdentry.get():
                        CTkMessagebox(master=frame,title="Error",message="Password and Confirm Password should be same",font=("",20),fg_color="black",
                                bg_color="black",text_color="purple",button_color="purple",button_hover_color="purple",button_text_color="black",
                                title_color="purple",cancel_button_color="purple",border_color="purple")
                elif my_check.get()=="OFF":
                        CTkMessagebox(master=frame,title="Error",message="Please agree to the Terms and Conditions.",font=("",20),fg_color="black",
                                bg_color="black",text_color="purple",button_color="purple",button_hover_color="purple",button_text_color="black",
                                title_color="purple",cancel_button_color="purple",border_color="purple")
                else:
                        conn=mysql.connector.connect(host="localhost",user="root",password="Shra@2807",database="cpp")#host="localhost",user="self",password="Shra@2807",database="mydata"
                        my_cursor=conn.cursor()
                        query=("select * from register where email=%s")
                        value=(emailentry.get(),)
                        my_cursor.execute(query,value)
                        row=my_cursor.fetchone()
                        if row !=None:
                                CTkMessagebox(master=frame,title="Error",message="User already exist,please try another Enrollment Number.",font=("",20),fg_color="black",
                                        bg_color="black",text_color="purple",button_color="purple",button_hover_color="purple",button_text_color="black",
                                        title_color="purple",cancel_button_color="purple",border_color="purple")
                        else:
                                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s)",
                                                (nameentry.get(),enrollentry.get(),emailentry.get(),contactentry.get(),
                                                pwdentry.get()))  
                                # if my_cursor>0:
                                #         CTkMessagebox(master=frame,title="Success",message="User Registered Successfully!",font=("",20),fg_color="black",
                                #         bg_color="black",text_color="purple",button_color="purple",button_hover_color="purple",button_text_color="black",
                                #         title_color="purple",cancel_button_color="purple",border_color="purple")     
                        conn.commit()
                        conn.close()
                CTkMessagebox(master=frame,title="Success",message="User Registered Successfully!",font=("",20),fg_color="black",
                                        bg_color="black",text_color="purple",button_color="purple",button_hover_color="purple",button_text_color="black",
                                        title_color="purple",cancel_button_color="purple",border_color="purple")
                        
        registerbtn = customtkinter.CTkButton(master=frame,text="Register Now", text_color="black",command=register_data,
                width=320,height=30,font=("",20),fg_color="purple",corner_radius=10,hover_color="purple")  
        registerbtn.place(x=30,y=530)
        
        def login_page():
                root.destroy()
                import login
                login_page_open=customtkinter.CTkToplevel(login.login_win)

        loginbtn = customtkinter.CTkButton(master=frame, text="Log In",text_color="black",command=login_page,
                width=320,height=30,font=("",20),fg_color="purple",corner_radius=10,hover_color="purple") 
        loginbtn.place(x=500,y=530)

                
        root.mainloop()

        
register_win()


