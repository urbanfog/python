from random import randint
from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password = []

    password += [random.choice(letters)
                 for _ in range(1, random.randint(8, 10) + 1)]
    password += [random.choice(symbols)
                 for _ in range(1, random.randint(2, 4) + 1)]
    password += [random.choice(numbers)
                 for _ in range(1, random.randint(2, 4) + 1)]

    random.shuffle(password)

    pw_input.insert(0, "".join(password))

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    '''Save password to text_file'''
    site = web_input.get()
    email = email_input.get()
    pw = pw_input.get()
    is_valid = validate(site, email, pw)
    if is_valid:
        is_ok = messagebox.askokcancel(title="Verify Your Info",
                                       message=f"These are the details entered:\nSite: {site}\nEmail: {email}\nPassword: {pw}")
        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{site} | {email} | {pw}\n")
            clear_entries()


def validate(site, email, pw):
    if len(site) == 0 or len(pw) == 0:
        messagebox.showwarning(
            title="Oops", message="Please don't leave any fields blank.")
        return False
    return True


def clear_entries():
    '''Clear website and password inputs'''
    web_input.delete(0, END)
    pw_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# Window Setup
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas widget
canvas = Canvas(width=200, height=200)
canvas.grid(row=0, column=0, columnspan=3)

# Image widget
image = PhotoImage(file="logo.gif")
canvas.create_image(100, 100, image=image)

web_label = Label(text="Website: ")
web_input = Entry(width=45)
web_input.focus()
web_label.grid(row=1, column=0)
web_input.grid(row=1, column=1, columnspan=2)

email_label = Label(text="Email/Username: ")
email_input = Entry(width=45)
email_input.insert(0, "james@email.com")
email_label.grid(row=2, column=0)
email_input.grid(row=2, column=1, columnspan=2)

pw_label = Label(text="Password: ")
pw_input = Entry(width=26)
pw_label.grid(row=3, column=0)
pw_input.grid(row=3, column=1)

pw_button = Button(text="Generate Password", command=generate_password)
pw_button.grid(row=3, column=2)
add_button = Button(text="Add", width=44, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
