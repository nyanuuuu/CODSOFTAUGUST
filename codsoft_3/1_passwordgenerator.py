# Import libraries:
import random
import string
from tkinter import *


# Function:
def generated_password():
    len = int(length_entry.get())
    if len <=0:
        result_label.config(text="Please enter a positive integer.")
    else:
         char = string.ascii_letters + string.digits + string.punctuation+ string.ascii_uppercase
         password ="".join(random.sample(char,len))
         result_label.config(text=password)

# Creating GUI window:
window = Tk()
window.title('//Password Generator//')
window.geometry("300x220")
icon = PhotoImage(file='icon5.png')
window.iconphoto(True, icon)
window.config(background="#85586F")

# Labels:
label = Label(window, text="Password Generator", font=("Times New Roman", 20, "bold"), bg="#DEB6AB", fg="Black")
label.pack(pady=10)

length_label = Label(window, text="Length of the password:",font=("Times New Roman", 14,  "bold"), bg="#85586F", fg="White")
length_label.pack(pady=3)
length_entry = Entry(window,width=20,font=("Times New Roman",12,"bold"))
length_entry.pack(pady=3)

# button:
generate_button = Button(window, text="Generate Password", command=generated_password,font=("Times New Roman", 10,  "bold"),bg="#DEB6AB")
generate_button.pack(pady=10)

result_label = Label(window, text="",width=25,font=("Times New Roman",12,"bold"))
result_label.pack()


window.mainloop()
