from tkinter import *

def generate_password():
    pass


window = Tk()
window.title("Password Manager")
# window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

canvas = Canvas(width=150, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo) #center to position
canvas.grid(row=0, column=1)

label_website = Label(text="Website")
label_website.grid(column=0, row=1)
input_website = Entry(width=35)
input_website.grid(column=1, row=1, columnspan=2)

label_email = Label(text="Email/Username")
label_email.grid(column=0, row=2)
input_email = Entry(width=35)
input_email.grid(column=1, row=2, columnspan=2)

label_pwd = Label(text="Password")
label_pwd.grid(column=0, row=3)
input_pwd = Entry(width=25)
input_pwd.grid(column=1, row=3)
button_generate = Button(text="Generate", highlightthickness=0, command=generate_password())
button_generate.grid(column=2, row=3)

button_add = Button(text="Add", command=generate_password())
button_add.grid(column=1, row=4, columnspan=2)

window.mainloop()