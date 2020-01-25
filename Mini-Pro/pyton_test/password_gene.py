# importer tkinter
import string
from random import choice, randint
from tkinter import *


class MyApp:

    def __init__(self):
        self.window = Tk()
        self.window.title("PasswordGenerator")
        self.window.geometry("600x480")
        self.window.maxsize(600, 480)
        self.window.config(background='#1f1f1f')
        self.create_widgets()
        self.create_frame()

    def create_widgets(self):
        
        self.create_main_logo()
        
    def create_frame(self):
        self.frame = Frame(self.window, bg="#1f1f1f")

        self.create_title()
        self.create_entry_input()
        self.create_generate_button("Générer")

        self.frame.pack(side=LEFT, expand=True, fill=X)
        

    def create_main_logo(self):
        width, height = 300, 300
        can = Canvas(self.window, width=width, height=height,bg="#1f1f1f", bd=0, highlightthickness=0)
        self.mon_image = PhotoImage(file="images/password.png").zoom(15).subsample(32)
        can.create_image(height / 2, width / 2, image=self.mon_image)
        can.pack(side=LEFT, expand=True, fill=X)

    def generate(self, min=12, max=17):
        list_ponct = ['*', ' %', '#', '?', '!', '$', '&',]
        all_char = choice(list_ponct) + string.ascii_letters + choice(list_ponct) + string.digits
        password = "".join(choice(all_char) for x in range(randint(min, max)))
        password_end = choice(list_ponct) + password
        self.entry.delete(0, END)
        self.entry.insert(0, password_end)

    def create_title(self):
        self.label_title = Label(self.frame, text="Mot de passe", font=("Helvetica", 20), bg="#1f1f1f", fg="#ffffff")
        self.label_title.pack()

    def create_entry_input(self):
        self.entry = Entry(self.frame , fg="#1f1f1f")
        self.entry.config(font=("Courier", 20))
        self.entry.pack()

    def create_generate_button(self, string):
        button = Button(self.frame, text=string, bg='#1f1f1f', fg='#1f1f1f', command=self.generate)
        button.config(font=("Courier", 30))
        button.pack()


# Create the entire GUI program
program = MyApp()

# Start the GUI event loop
program.window.mainloop()