import tkinter as tk
import tkinter.font as tfont


window=tk.Tk()
window.title("My Application")
window.minsize(width=500 , height=500)

custom_font=tfont.Font(family="Times New Roman",size=15,slant=tfont.ITALIC)
custom_font1=tfont.Font(family="Times New Roman",size=20,weight=tfont.BOLD)

label=tk.Label(text="Hello How are you",font=custom_font,bg="lightblue",fg="darkblue")
label.pack(side="top")

label1=tk.Label(text="Hello World !",font=custom_font1)
label1.pack(side="bottom")

label2=tk.Label(text="Beta how are you")
label2.pack(expand="true")
label2.config(font=("Courier New",25),text="My new app")

label["text"]="Have a nice day" # change the text

counter=0;
def click_button():
    global counter
    counter+=1;
    label.config(text=f"thanks for clicking {counter} time")
    label.pack(side="right")


#Buttons
button=tk.Button(text="Click",command=click_button)
button.pack(expand="true")

#Taking user input using entry

user_input=tk.Entry(width=30)
user_input.pack()
print(user_input.get())

window.mainloop()