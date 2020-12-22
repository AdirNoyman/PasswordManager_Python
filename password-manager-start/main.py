from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    input_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    search_term = input_website.get().title()
    print(search_term)
    try:
        with open('password_data.json', mode='r') as data_file:
            data = json.load(data_file)
            print(data)
            info = data[search_term]
    except FileNotFoundError:
        messagebox.showerror("NO PASSWORDS", "Sorry, passwords data is empty ☹️")
        return
    except KeyError:
        messagebox.showerror("NOT FOUND", f"Sorry, didn't find data for {search_term} website ☹️")
        return
    else:
        messagebox.showinfo(title=data[search_term], message=f"Email: {info['email']}\nPassword: {info['password']}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    website = input_website.get().title()
    email = input_Email.get()
    password = input_password.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror("Oopsss...", "Hey DUMB ASS fill all the fields! 🤬")
        return
    answer = messagebox.askyesno(title=website.title(), message=f"Would you like to save this data?\nWebsite: {website}\nEmail\\User: {email}\nPassword: {password}")
    if answer:
        try:
            with open('password_data.json', mode='r') as data_file:
                # Reading the old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open('password_data.json', mode='w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating the old data
            data.update(new_data)
            with open('password_data.json', mode='w') as data_file:
                # Saving the updated data
                json.dump(data, data_file, indent=4)
        finally:
            input_website.delete(0, END)
            input_password.delete(0, END)


def clear_data():
    input_website.delete(0, END)
    input_Email.delete(0, END)
    input_password.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
root = window
window.title("Password Manager")
window.config(padx=50,pady=50,width=500,height=500)


canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 90, image=lock_image)
canvas.grid(column=1,row=0)

label_website = Label(text="Website:", fg="purple", font=('Arial', 18, 'bold'))
label_website.grid(column=0,row=1)

input_website = Entry(width=21)
input_website.grid(column=1,row=1)
input_website.focus()

button_search = Button(text="Search Password", width=13, command=search_password)
button_search.grid(column=2, row=1, columnspan=1)


label_Email = Label(text="Email/Username:", fg="purple", font=('Arial', 18, 'bold'))
label_Email.grid(column=0,row=2)

input_Email = Entry(width=35)
input_Email.grid(column=1,row=2, columnspan=2)
input_Email.insert(0, "koko@gmail.com")

label_password = Label(root,text="Password:", fg="purple", font=('Arial', 18, 'bold'))
label_password.grid(column=0,row=3)

input_password = Entry(width=21)
input_password.grid(column=1,row=3)

button_password = Button(text="Generate Password", fg='blue',command=generate_password)
button_password.grid(column=2,row=3,columnspan=1)

button_add = Button(text="Clear",fg='blue', width=41,command=clear_data,font=('Arial',14))
button_add.grid(column=1,row=4,columnspan=2)

button_add = Button(text="Add",fg='red', width=41,command=add_data,font=('Arial',14))
button_add.grid(column=1,row=5,columnspan=2)




window.mainloop()

