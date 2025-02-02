from tkinter import *
import customtkinter
from PIL import Image
from CTkMessagebox import CTkMessagebox
import os
import numpy as np


customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
        
        
def main_win():
                main=customtkinter.CTk()    
                main.title("Smart Attendence Management System")
                main.geometry("1280x1080")

                img= customtkinter.CTkImage(light_image=Image.open("D:\\Face Recognition Attendance System Project\\Images_GUI\\bg.jpg"),
                        dark_image=Image.open("D:\\Face Recognition Attendance System Project\\Images_GUI\\bg.jpg"),size=(1550,800))
                lbl=customtkinter.CTkLabel(main,image=img)
                lbl.place(x=0,y=0,relwidth=1,relheight=1)

                mainframe=customtkinter.CTkFrame(main,width=1002,height=652,corner_radius=0,fg_color="white",border_width=5,border_color="black")
                mainframe.place(x=180,y=50)

                imgI= customtkinter.CTkImage(light_image=Image.open("Images_GUI\\bg.jpg"),#"C:\Users\shrav\Downloads\bg4.jpg"
                        dark_image=Image.open("Images_GUI\\bg.jpg"),size=(996,646))
                lblI=customtkinter.CTkLabel(mainframe,text="",image=imgI)
                lblI.place(x=3,y=3)
                imgI= customtkinter.CTkImage(light_image=Image.open("Images_GUI\\cppname2.png"),
                        dark_image=Image.open("Images_GUI\\cppname2.png"),size=(996,80))
                lblI=customtkinter.CTkLabel(mainframe,text="",image=imgI)
                lblI.place(x=3,y=2)
                

                def open_img():
                        os.startfile("Image_Dataset")
                        main.mainloop()
                        


                def Student_page(root):
                        import student
                        student.Student(root)
                        main.mainloop()



                def Detection_Page(root):
                        import face_detect
                        face_detect.Face_Recognition(root)
                        main.mainloop()


                img1= customtkinter.CTkImage(light_image=Image.open("Images_GUI\\stud.png"),
                        dark_image=Image.open("Images_GUI\\stud.png"),size=(160,160))
                studbtn = customtkinter.CTkButton(master=mainframe,text="",image=img1,command=lambda: Student_page(main),
                                                bg_color="black",fg_color="black",hover_color="black") 
                studbtn.place(x=70,y=100)
                studlbl=customtkinter.CTkLabel(master=mainframe,text="Student Details",font=("",20),fg_color="black"
                                                ,bg_color="black",text_color="purple",width=177)
                studlbl.place(x=70,y=260)
                
                
                img2= customtkinter.CTkImage(light_image=Image.open("Images_GUI\\facerecogn.png"),
                        dark_image=Image.open("Images_GUI\\facerecogn.png"),size=(160,160))
                facebtn = customtkinter.CTkButton(master=mainframe,text="",image=img2,command=lambda: Detection_Page(main),
                                                bg_color="black",fg_color="black",hover_color="black") 
                facebtn.place(x=320,y=100)
                facelbl=customtkinter.CTkLabel(master=mainframe,text="Face Detector",font=("",20),fg_color="black"
                                                ,bg_color="black",text_color="purple",width=177)
                facelbl.place(x=320,y=260)


                def go_to_atten(root):
                        import attendance
                        attendance.Attendance(root)
                        main.mainloop()
                
                
                img3= customtkinter.CTkImage(light_image=Image.open("Images_GUI\\attendence.png"), 
                        dark_image=Image.open("Images_GUI\\attendence.png"),size=(160,160))
                atdbtn = customtkinter.CTkButton(master=mainframe,text="", command=lambda: go_to_atten(main), image=img3,#height=90,width=80,corner_radius=20,
                                                bg_color="black",fg_color="black",hover_color="black") 
                atdbtn.place(x=550,y=100)
                atdlbl=customtkinter.CTkLabel(master=mainframe,text="Attendence",font=("",20),fg_color="black"
                                                ,bg_color="black",text_color="purple",width=177)
                atdlbl.place(x=550,y=260)


                def train_data(root):
                        import train
                        train.Train(root)
                        main.mainloop()


                img4=customtkinter.CTkImage(light_image=Image.open("Images_GUI\\data.png"),
                        dark_image=Image.open("Images_GUI\\data.png"),size=(160,160))
                trainbtn = customtkinter.CTkButton(master=mainframe,text="",image=img4,command=lambda: train_data(main),
                                                bg_color="black",fg_color="black",hover_color="black")
                trainbtn.place(x=780,y=100)
                trainlbl=customtkinter.CTkLabel(master=mainframe,text="Train data",font=("",20),fg_color="black"
                                                ,bg_color="black",text_color="purple",width=177)
                trainlbl.place(x=780,y=260)  
                
                

                img5=customtkinter.CTkImage(light_image=Image.open("Images_GUI\\photo.jpg"),
                        dark_image=Image.open("Images_GUI\\photo.jpg"),size=(160,160))
                photosbtn = customtkinter.CTkButton(master=mainframe,text="",image=img5,command=open_img,
                                                bg_color="black",fg_color="black",hover_color="black")
                photosbtn.place(x=70,y=400)
                photoslbl=customtkinter.CTkLabel(master=mainframe,text="Photos",font=("",20),fg_color="black"
                                                ,bg_color="black",text_color="purple",width=177)
                photoslbl.place(x=70,y=560)


                def go_to_dev(root):
                        import developer
                        developer.Developer(root)
                        main.mainloop()
                
                
                img6= customtkinter.CTkImage(light_image=Image.open("Images_GUI\\dev.png"),
                        dark_image=Image.open("Images_GUI\\dev.png"),size=(160,160))
                devbtn = customtkinter.CTkButton(master=mainframe,text="",image=img6,command=lambda: go_to_dev(main),
                                                bg_color="black",fg_color="black",hover_color="black") 
                devbtn.place(x=320,y=400)
                devlbl= customtkinter.CTkLabel(mainframe,text="Developers",font=("Times new roman",20), bg_color="black",text_color="purple",width=177) 
                devlbl.place(x=320,y=560)


                def go_to_help():
                        import help
                        help.create_help_page()
                        main.destroy()
                
                
                img7= customtkinter.CTkImage(light_image=Image.open("Images_GUI\\help.png"),
                        dark_image=Image.open("Images_GUI\\help.png"),size=(160,160))
                helpbtn = customtkinter.CTkButton(master=mainframe,text="",image=img7,command=go_to_help,
                                                bg_color="black",fg_color="black",hover_color="black") 
                helpbtn.place(x=550,y=400)
                helplbl=customtkinter.CTkLabel(master=mainframe,text="Help",font=("",20),fg_color="black"
                                                ,bg_color="black",text_color="purple",width=177)
                helplbl.place(x=550,y=560)
                


                # Exit Button

                img8= customtkinter.CTkImage(light_image=Image.open("Images_GUI\\exit.png"),
                        dark_image=Image.open("Images_GUI\\exit.png"),size=(160,160))
                exitbtn = customtkinter.CTkButton(master=mainframe,text="",image=img8,command=exit,
                                                bg_color="black",fg_color="black",hover_color="black") 
                exitbtn.place(x=780,y=400)
                exitlbl=customtkinter.CTkLabel(master=mainframe,text="Exit",font=("",20),fg_color="black"
                                                ,bg_color="black",text_color="purple",width=177)
                exitlbl.place(x=780,y=560)

                

                main.mainloop()
        

main_win()