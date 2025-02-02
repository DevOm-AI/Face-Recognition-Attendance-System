from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
import os

class Train:
    def __init__(self,root):
        self.root=root
        self.root.state("zoomed")
        self.root.title("Data Train Panel")


        # Background Image Setup
        bg1=Image.open("Images_GUI\\bg.jpg")
        bg1=bg1.resize((1920,1080),Image.NEAREST)
        photobg1=ImageTk.PhotoImage(bg1)

        bg_img = Label(root,image=photobg1)
        bg_img.place(x=0,y=0,width=1920,height=1080)


        #title section
        title_lb1 = Label(root,text="Train Dataset Panel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=100,width=1366,height=45)

        # Student Imamge Button
        std_img_btn=Image.open("Images_GUI\\data.png")
        std_img_btn=std_img_btn.resize((180,180),Image.NEAREST)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(self.root, command=self.train_classifier, image=self.std_img1,cursor="hand2")
        std_b1.place(x=550,y=225,width=180,height=180)

        std_b1_1 = Button(self.root, command=self.train_classifier,text="Train Dataset",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=550,y=400,width=180,height=45)


    def train_classifier(self):
        data_dir=("Image_Dataset")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
            
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # conver in gray scale 
            imageNp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
            
        ids=np.array(ids)
            
        #=================Train Classifier=============
        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("clf.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset Complated!",parent=self.root)

        




if __name__ == "__main__":
    root = Tk()
    Train(root)
    root.mainloop()