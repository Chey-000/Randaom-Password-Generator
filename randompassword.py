from tkinter import *
import string
import random
import pyperclip
def generator():
    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    numbers=string.digits
    special_characters=string.punctuation                               #lOGICAL ANALYSIS#
    all=small_alphabets+capital_alphabets+numbers+special_characters
    password_length=int(length_Box.get())

    if choice.get()==1:
        passwordField.insert(0,random.sample(small_alphabets,password_length))
    if choice.get()==2:
        passwordField.insert(0,random.sample(small_alphabets+capital_alphabets,password_length))
    if choice.get()==3:
        passwordField.insert(0,random.sample(all,password_length))        #LOGICAL OPERATION#


def copy():
    random_password=passwordField.get()        #TO COPY THE TEXT#
    pyperclip.copy(random_password)



root=Tk()
choice=IntVar()
Font=('arial',15,'bold')
root.config(background='#263045')
passwordLable=Label(root, text='Password Generator', font=('times new roman', 25 , 'bold'),background='#263045',fg='white')
passwordLable.grid(pady=10)    #TO DISPLAY#
weakradioButton=Radiobutton(root,text='Weak',value=1, variable=choice, font=Font)
weakradioButton.grid(pady=5)
mediumradioButton=Radiobutton(root,text='Medium',value=2, variable=choice, font=Font)
mediumradioButton.grid(pady=5)
strongradioButton=Radiobutton(root,text='Strong',value=3, variable=choice, font=Font)
strongradioButton.grid(pady=5)
lengthLable=Label(root, text='Password Length', font=Font,background='#263045',fg='white')
lengthLable.grid(pady=5)
length_Box=Spinbox(root,from_=5,to_=18,width=5,font=Font)
length_Box.grid(pady=5)
generateButton=Button(root,text='Generate',font=Font, command=generator)
generateButton.grid(pady=5)
passwordField=Entry(root,width=25,bd=2,font=Font)
passwordField.grid(pady=5)
copyButton=Button(root,text='Copy',font=Font,command=copy)
copyButton.grid(pady=5)
root.mainloop()