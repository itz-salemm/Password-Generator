from tkinter import *
import random

#To Generate the Password
def generate():
	global passwr
	alphabets="abcdefghijklmnopqrstuvwxyz"
	numbers = "1234567890"
	symbols ="!@#$%^&*()"
	passw = alphabets + numbers + symbols
	passwr = "".join(random.sample(passw,8))
	p = "shkgj"
	password.set(passwr)


#UI Designs 
root = Tk()
root.title("Password Generator")
root.geometry("500x200")
title = Label(root, text="Random Password Generator?", bg="black", fg="white").pack()
password = StringVar()


result= Entry(root, textvariable=password,  font=('arial', 20, 'bold'), justify=CENTER).pack()
gen = Button(root, text="Generate", bg="light green", fg="black", command=lambda:generate()).pack()

root.mainloop()