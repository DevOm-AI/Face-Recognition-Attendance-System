from tkinter import * 
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter as tk

def create_help_page():
    """Creates the Tkinter window and widgets for the help page."""
    root = tk.Tk()
    root.title("Help Page")
    root.state("zoomed")

    # background image 
    bg1=Image.open(r"Images_GUI\\bg.jpg")
    bg1=bg1.resize((1920,810),Image.NEAREST)
    photobg1=ImageTk.PhotoImage(bg1)

    # set image as lable
    bg_img = Label(root,image=photobg1, bg='black')
    bg_img.place(x=0,y=0,width=1920,height=810)

    # Create a frame with padding for content
    content_frame = tk.Frame(root, bg="white", padx=50, pady=50, bd=10, relief="solid")
    content_frame.place(x=300, y=150)

    # Heading with a larger font and bold style
    heading_label = tk.Label(content_frame, text="Help and Support", font=("Arial", 24, "bold"), fg="black")
    heading_label.grid(row=0, column=0, columnspan=2, pady=(30, 10))

    # Personal Information
    personal_info_frame = tk.Frame(content_frame, bg="white")
    personal_info_frame.grid(row=1, column=0, padx=(0, 50), pady=(10, 10), sticky="w")

    tk.Label(personal_info_frame, text="Shravni K", font=("Arial", 18, "bold"), fg="black").grid(row=0, column=0, pady=(0, 10))
    tk.Label(personal_info_frame, text="shravnik@gmail.com", font=("Arial", 14, "bold"), fg="black").grid(row=1, column=0, pady=(0, 10))

    personal_info_frame.grid_columnconfigure(0, weight=1)

    # Friend Information
    friend_info_frame = tk.Frame(content_frame, bg="white")
    friend_info_frame.grid(row=1, column=1, padx=(50, 0), pady=(10, 10), sticky="e")

    tk.Label(friend_info_frame, text="Shravni Friend", font=("Arial", 18, "bold"), fg="black").grid(row=0, column=0, pady=(0, 10))
    tk.Label(friend_info_frame, text="shravnifriend@gmail.com", font=("Arial", 14, "bold"), fg="black").grid(row=1, column=0, pady=(0, 10))

    friend_info_frame.grid_columnconfigure(0, weight=1)

    root.mainloop()

# Create the help page
create_help_page()