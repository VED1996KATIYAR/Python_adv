import tkinter as tk
import tkinter.font as tfont

window=tk.Tk()
window.title("My Application")
window.minsize(width=500,height=600)

custom_font=tfont.Font(family="Times New Roman",size=15,slant=tfont.ITALIC)
custom_font1=tfont.Font(family="Times New Roman",size=20,weight=tfont.BOLD)

label=tk.Label(text="Hello How are you",font=custom_font,bg="violet" ,fg="blue")
label.pack(side="left")

label1=tk.Label(text="Hello World",font=custom_font1)
label1.pack(side="right")

#buttons
counter=0
def click():
    global counter
    counter+=1;
    label.config(text=f"Thanks for clicking {counter} times")

button=tk.Button(text="Click",command=click)
button.pack(side="bottom")

#Taking user input using entry
#Phele entry aur label banaye
user_input=tk.Entry(width=10)
user_input.pack(pady=30)

label=tk.Label(text="Yahan text aayega")
label.pack(pady=10)

#Phir function banaye jo data uthaye
def user1():
    text_value=user_input.get()
    label.config(text=text_value)

#ab buttone bano
button1=tk.Button(text="Click1",command=user1)
button1.pack(expand=True)







window.mainloop()