# Importing libraries:
from tkinter import *
from tkinter.font import Font

# Functions:
def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)

def update_item():
    selected_item = my_list.curselection()
    if selected_item:
        updated_text = my_entry.get()
        if updated_text:
            my_list.delete(selected_item)
            my_list.insert(selected_item, updated_text)
            my_entry.delete(0, END)

def crossoff_item():
    my_list.itemconfig(my_list.curselection(), {'fg':'black'})
    # get rid of selection bar:
    my_list.selection_clear(0, END)

def uncross_item():
    my_list.itemconfig(my_list.curselection(), {'fg':'#964B00'})
    # get rid of selection bar:
    my_list.selection_clear(0, END)

def delete_item():
    my_list.delete(my_list.curselection())

def clear_list():
    my_list.delete(0, END)

def save_list():
    with open("todolist.txt", "w") as file:
        for item in my_list.get(0, END):
            file.write(item + "\n")

# Creating GUI window:
window = Tk()
window.title('//TO-DO LIST//')
window.geometry("580x550")
icon = PhotoImage(file='icon.png')
window.iconphoto(True, icon)
window.config(background="#DFCCA6")

# Fonts:
font = Font(family="Times New Roman", size=12, weight="bold")

# Create a label :
label = Label(window, text="To-Do List", font=("Times New Roman", 20, "italic bold"), bg="#DFCCA6", fg="Brown")
label.pack(pady=10)

# Frame:
my_frame = Frame(window, background="#DFCCA6")
my_frame.pack(pady=10)

# Listbox:
my_list = Listbox(my_frame, font=font, width=35, height=8, bg="SystemButtonFace", bd=0,
                  fg="#964B00", highlightthickness=0, selectbackground="#8A3324",
                  activestyle="none")
my_list.pack(side=LEFT, fill=BOTH)

stuff = ["Start with  task 2", "Upload Expts", "Create ppt", "Complete pending assignments,","Take a Nap","Clean your Room","Post updates on Linkedin"]

for item in stuff:
    my_list.insert(END, item)

# Create scrollbar:
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)

# Add scrollbar:
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

# Create an entry box:
my_entry = Entry(window, font=("Times New Roman", 18), fg="#964B00")
my_entry.pack(pady=20)

# Create a button frame:
button_frame = Frame(window, background="#DFCCA6")
button_frame.pack(pady=20)

# Create two sub-frames:
button_frame1 = Frame(button_frame, background="#DFCCA6")
button_frame1.pack(pady=10)

button_frame2 = Frame(button_frame, background="#DFCCA6")
button_frame2.pack(pady=10)

# Add buttons to button_frame1:
add_button = Button(button_frame1, text="Add ", command=add_item, bg="#DFCCA6", fg="#964B00", font=("Times New Roman", 12, "bold"))
update_button = Button(button_frame1, text="Update ", command=update_item, bg="#DFCCA6", fg="#964B00", font=("Times New Roman", 12, "bold"))
crossoff_button = Button(button_frame1, text="Checked", command=crossoff_item, bg="#DFCCA6", fg="#964B00", font=("Times New Roman", 12, "bold"))
uncross_button = Button(button_frame1, text="Unchecked ", command=uncross_item, bg="#DFCCA6", fg="#964B00", font=("Times New Roman", 12, "bold"))

add_button.grid(row=0, column=0)
update_button.grid(row=0, column=1, padx=20)
crossoff_button.grid(row=0, column=2)
uncross_button.grid(row=0, column=3, padx=20)

# Add buttons to button_frame2:
delete_button = Button(button_frame2, text="Delete ", command=delete_item, bg="#DFCCA6", fg="#964B00", font=("Times New Roman", 12, "bold"))
clearlist_button = Button(button_frame2, text="Clear List", command=clear_list, bg="#DFCCA6", fg="#964B00", font=("Times New Roman", 12, "bold"))
save_list_button = Button(button_frame2, text="Save List", command=save_list, bg="#DFCCA6", fg="#964B00", font=("Times New Roman", 12, "bold"))

delete_button.grid(row=0, column=0)
clearlist_button.grid(row=0, column=1, padx=20)
save_list_button.grid(row=0, column=2)

window.mainloop()
