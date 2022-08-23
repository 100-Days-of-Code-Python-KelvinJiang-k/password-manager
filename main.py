from tkinter import *
from tkinter import messagebox
from password_generator import PasswordGenerator
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
password_generator = PasswordGenerator()


def generate_password():
    password = password_generator.generate()
    pyperclip.copy(password)
    password_entry.delete(0, END)
    password_entry.insert(END, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def clear():
    website_entry.delete(0, END)
    password_entry.delete(0, END)


def save():
    website = website_entry.get()
    password = password_entry.get()
    email = email_entry.get()

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showerror(title="Error", message="You have invalid inputs")
        return

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n"
                                                          f"Email: {email}\nPassword: {password}"
                                                          f"\nDo you wish to save?")
    if is_ok:
        with open("passwords.txt", "a") as file:
            file.write(f"{website} | {email} | {password}\n")
        clear()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=36)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=36)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(END, "test@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Buttons
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)
add_data_button = Button(text="Add", width=36, command=save)
add_data_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
