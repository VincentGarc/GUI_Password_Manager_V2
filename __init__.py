import json
from tkinter import *
import string
import random
from tkinter import messagebox
import pyperclip
import json


def generate():
    alpha = list(string.ascii_letters)
    number = list(string.digits)
    simbol = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    chars = alpha + number + simbol
    password_input.delete(0, END)
    list_pass = [random.choice(chars) for n in range(15)]
    password_out = ''.join(list_pass)
    print(password_out)
    password_input.insert(0, password_out)
    pyperclip.copy(password_out)


def saver():
    website = website_input.get()
    email = email_user_input.get()
    password = password_input.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if website == "" or password == "":
        messagebox.showinfo(title='Oops', message="Please don't leave any fields empty!")
    else:
        try:
            with open("file/data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("file/data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)

            with open("file/data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# def find_password():
#     website = website_input.get()
#     with open("file/data.json", "r") as data_file:
#         data = json.load(data_file)
#
#     user_find = data[website]['email']
#     pass_find = data[website]['password']
#
#     if website_input.get() in data_file:
#         messagebox.showinfo(title='Pass find', message=f'User: {user_find}\nPass: {pass_find}')
#     else:
#         messagebox.showinfo(title='Pass not fund', message='No details for the website exist.')
def find_password():
    website = website_input.get()
    try:
        with open("file/data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


window = Tk()
button = Button()
label = Label()

window.title("Password Manager")
window.config(padx=20, pady=20)
window.iconbitmap('logo.ico')

logo = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=0, row=0, columnspan=3)

website_label = Label(text='Website: ', font='Arial')
website_label.grid(column=0, row=1)
email_user_label = Label(text='Email/Username: ', font='Arial')
email_user_label.grid(column=0, row=2)
password_label = Label(text='Password: ', font='Arial')
password_label.grid(column=0, row=3, columnspan=1)

website_input = Entry(width=27)
website_input.grid(column=1, row=1)
website_input.focus()
email_user_input = Entry(width=44)
email_user_input.insert(0, 'example@mail.com')  # If you want to set a default change the email
email_user_input.grid(column=1, row=2, columnspan=2)
password_input = Entry(width=27)
password_input.grid(column=1, row=3)

button_pass = Button(text='Generate Pass', width=13, border=0.5, pady=0, command=generate)
button_pass.grid(column=2, row=3)

button_add = Button(text='Add', font='Arial', width=10, border=0.5, pady=5, command=saver)
button_add.grid(column=1, row=4)

button_search = Button(text='Search', width=13, border=0.5, command=find_password)
button_search.grid(column=2, row=1)

window.mainloop()
