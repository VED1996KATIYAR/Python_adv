import tkinter as tk
window=tk.Tk()

window.minsize(width=200,height=200)
#Taking user input using entry
#Phele entry aur label banvae
user_input=tk.Entry(width=10)
user_input.pack(pady=10)
label=tk.Label(text="Yahan text aayega")
label.pack(pady=10)

def user1():
    text_value=user_input.get()
    label.config(text=text_value)

#ab button banao
button=tk.Button(text="Click1",command=user1)
button.pack(pady=10)


#quit button
quit_button=tk.Button(text="Quit",command=window.destroy)
quit_button.pack()

window.mainloop()