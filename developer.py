from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
import webbrowser

class Developer:
    def __init__(self,root):
        self.root=root
        #self.root.geometry("1366x768+0+0")
        self.root.state("zoomed")
        self.root.title("Developers")


        # backgorund image 
        bg1=Image.open(r"Images_GUI\\bg.jpg")
        bg1=bg1.resize((1920,810),Image.NEAREST)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=0,width=1920,height=810)

        #title section
        title_lb1 = Label(bg_img,text="Developer Panel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=200,y=50,width=1000,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 


        def gmail():
            new = 1
            url = "https://www.gmail.com"
            webbrowser.open(url,new=new)


        # Detect Face  button 2
        det_img_btn=Image.open(r"Images_GUI\\usericon1.jpg")
        det_img_btn=det_img_btn.resize((180,180),Image.NEAREST)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img, command=gmail, image=self.det_img1,cursor="hand2",)
        det_b1.place(x=360,y=300,width=180,height=180)

        det_b1_1 = Button(bg_img,text="Shravani Kavle", command=gmail, cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        det_b1_1.place(x=360,y=480,width=180,height=55)


        # Attendance System  button 3
        att_img_btn=Image.open(r"Images_GUI\\usericon1.jpg")
        att_img_btn=att_img_btn.resize((180,180),Image.NEAREST)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img, command=gmail, image=self.att_img1,cursor="hand2",)
        att_b1.place(x=790,y=300,width=180,height=180)

        att_b1_1 = Button(bg_img,text="Bhakti Bhoskar", command=gmail, cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        att_b1_1.place(x=790,y=480,width=180,height=45)


        # Here a code snippet if you want to add any other developer's information
        # Just have a special focus on x coordinates

        # std_img_btn=Image.open("Place_Your_Image")
        # std_img_btn=std_img_btn.resize((180,180),Image.NEAREST)
        # self.std_img1=ImageTk.PhotoImage(std_img_btn)

        # std_b1 = Button(bg_img,image=self.std_img1,cursor="hand2")
        # std_b1.place(x,y,width,height)

        # std_b1_1 = Button(bg_img,text,cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        # std_b1_1.place(x,y,width,height)



if __name__ == "__main__":
    root=Tk()
    Developer(root)
    root.mainloop()
