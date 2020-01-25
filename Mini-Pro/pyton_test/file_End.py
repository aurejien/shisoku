from tkinter import *
from random import randint, choice
import string



class MyApp:

    def __init__(self):
        self.window = Tk()
        self.window.title('Générateur de mot de passe')
        self.window.geometry("720x480")
        self.window.minsize(720, 480)
        self.window.config(background='#1f1f1f')

        # la frame
        self.frame = Frame(self.window, bg="#1f1f1f")

        self.create_widgets()

        self.frame.pack(side=LEFT, expand=True, fill=X)
    
    def create_widgets(self):
        self.create_image()
        self.create_right_frame()
        self.create_title()
        self.password_generat()
        self.create_password()


    
    def create_image(self):
        width = 300
        height = 300
        self.image = PhotoImage(file="images/password.png").zoom(15).subsample(32)
        self.canvas = Canvas(self.frame, width=width, height=height,bg="#1f1f1f", bd=0, highlightthickness=0)
        self.canvas.create_image(width/2, height/2, image=self.image)
        self.canvas.pack()
        

    def create_right_frame(self):
        # la frame de droite
        self.right_frame = Frame(self.window, bg="#1f1f1f")
        self.right_frame.pack(side=LEFT, expand=True, fill=X)

    def create_title(self):
        # Le titre
        self.label_title = Label(self.right_frame, text="Mot de passe", font=("Helvetica, 20"), bg="#1f1f1f", fg="#ffffff")
        self.label_title.pack()
        # l'input

    def password_generat(self):
        password_min = 6
        password_max = 12
        all_charts = string.hexdigits + string.punctuation
        password = "".join(choice(all_charts) for x in range(randint(password_min, password_max)))
        
        
    def create_password(self):
        password_entry = Entry(self.right_frame, font=("Helvetica, 20"), bg="#1f1f1f", fg="#ffffff" )
        password_entry.pack()
        password_entry.delete(0, END)
        password_entry.insert(0, password)
    
    def creat_button(self):
        
        # le boutton
        button_gen = Button(self.right_frame, text="Générer", font=("Helvetica, 20"), bg="#1f1f1f", fg="#1f1f1f", command=self.password_generat)
        button_gen.pack()




app = MyApp()
app.window.mainloop()