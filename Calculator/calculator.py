# Importing libraries:
from tkinter import *
from tkinter.font import Font

# Creating GUI window:
window = Tk()
window.title('//Calculator//')
window.geometry("600x620+420+60")
icon = PhotoImage(file='icon2.png')
window.iconphoto(True, icon)
window.config(background="#654321")

# Functions:
equation = " "
def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)
    
def clear():
    global equation
    equation = ""
    label_result.config(text=equation)
    
def calculate():
    global equation
    result=""
    if equation !="":
      try:
            result=eval(equation)
      except:
          result="error"
          equation= ""
    label_result.config(text=result)
    
# creating label:
label_result = Label(window, width=23, height=2, text="", font=("Times New Roman", 30, "bold"), bg="#D2B48C")
label_result.pack(padx=25, pady=20)  

# buttons:


button = Button(window, text="C", width=5, height=1, bd=2, bg="#DAA06D", fg="#964B00",font=("Times New Roman", 30, "bold"),command =lambda:clear()) .place(x=20, y=140)  
button = Button(window, text="/", width=5, height=1, bd=2, bg="#DFCCA6", fg="#964B00", font=("Times New Roman", 30, "bold"),command =lambda:show("/")).place(x=160, y=140)  
button = Button(window, text="%", width=5, height=1, bd=2, bg="#DFCCA6", fg="#964B00", font=("Times New Roman", 30, "bold"),command =lambda:show("%")).place(x=300, y=140)  
button = Button(window, text="*", width=5, height=1, bd=2, bg="#DFCCA6", fg="#964B00", font=("Times New Roman", 30, "bold"),command =lambda:show("*")).place(x=440, y=140)  

button = Button(window, text="7", width=5, height=1, bd=2, bg="#F5F5DC", fg="#964B00", font=("Times New Roman", 30, "bold"),command =lambda:show("7")).place(x=20, y=230)  
button = Button(window, text="8", width=5, height=1, bd=2, bg="#F5F5DC", fg="#964B00", font=("Times New Roman", 30, "bold"),command =lambda:show("8")).place(x=160, y=230)  
button = Button(window, text="9", width=5, height=1, bd=2, bg="#F5F5DC", fg="#964B00", font=("Times New Roman", 30, "bold"),command =lambda:show("9")).place(x=300, y=230)  
button = Button(window, text="-", width=5, height=1, bd=2, bg="#DFCCA6", fg="#964B00", font=("Times New Roman", 30, "bold"),command =lambda:show("-")).place(x=440, y=230)  

button = Button(window, text="4", width=5, height=1, bd=2, bg="#F5F5DC", fg="#964B00", font=("Times New Roman", 30, "bold"),command =lambda:show("4")).place(x=20, y=320)  
button = Button(window, text="5", width=5, height=1, bd=2, bg="#F5F5DC", fg="#964B00", font=("Times New Roman", 30, "bold"),command =lambda:show("5")).place(x=160, y=320)  
button = Button(window, text="6", width=5, height=1, bd=2, bg="#F5F5DC", fg="#964B00", font=("Times New Roman", 30, "bold"),command =lambda:show("6")).place(x=300, y=320)  
button = Button(window, text="+", width=5, height=1, bd=2, bg="#DFCCA6", fg="#964B00", font=("Times New Roman", 30, "bold"),command =lambda:show("+")).place(x=440, y=320)  

button = Button(window, text="1", width=5, height=1, bd=2, bg="#F5F5DC", fg="#964B00", font=("Times New Roman", 30, "bold"),command =lambda:show("1")).place(x=20, y=410)  
button = Button(window, text="2", width=5, height=1, bd=2, bg="#F5F5DC", fg="#964B00", font=("Times New Roman", 30, "bold"),command =lambda:show("2")).place(x=160, y=410)  
button = Button(window, text="3", width=5, height=1, bd=2, bg="#F5F5DC", fg="#964B00", font=("Times New Roman", 30, "bold"),command =lambda:show("3")).place(x=300, y=410)  
button = Button(window, text="0", width=11, height=1, bd=2, bg="#F5F5DC", fg="#964B00", font=("Times New Roman", 30, "bold"),command =lambda:show("0")).place(x=15, y=500)  

button = Button(window, text=".", width=5, height=1, bd=2, bg="#F5F5DC", fg="#964B00", font=("Times New Roman", 30, "bold"),command =lambda:show(".")).place(x=300, y=500)  
button = Button(window, text="=", width=5, height=3, bd=2, bg="#DFCCA6", fg="#964B00", font=("Times New Roman", 30, "bold"),command =lambda:calculate()).place(x=440, y=410)  


window.mainloop()






