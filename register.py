from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

from PIL import  Image, ImageTk

def register_form(window, mainWindow, state, logo, _default_profile):
    window.resizable(False, False)
    window.iconbitmap('./reserved/icon.ico')
    # setting the properties of the window
    window.title("Register")
    # --------------
    w = 500
    h = 670
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    position_from_top = int(screen_height / 2 - h / 2)
    position_from_right = int(screen_width / 2 - w / 2)
    window.geometry("{}x{}+{}+{}".format(w, h, position_from_right, position_from_top))

    username_1 = "Banele"
    password_1 = "Banele_of_@stro"
    # ---------
    window.resizable(False, False)
    window.protocol('WM_DELETE_WINDOW', lambda: close())
    # login
    def register(username: str, password: str):
        # ' useRname    ' -> ' username    ' -> 'username'
        if username.lower().strip() == username_1 and password == password_1:
            # open main app
            error.config(text="")
            messagebox.showinfo("App", "You are logged in.")
        else:
            error.config(text="Invalid credentials.")


    # closing the window
    def close():
        res = messagebox.askyesnocancel("Close Register Form", "Are you sure you want to close this register form?")
        if res == True:
            state.setOpen(False)
            window.destroy()
        else:
            window.focus()
    # hiding and showing passwords
    def hide_show_1():
        if pass_ey_1.get() == True:
            password.config(show="")
            eye_1.config(text="Hide Password")
        else:
            password.config(show="*")
            eye_1.config(text="Show Password")


    def hide_show_2():
        if pass_ey_2.get() == True:
            conf_password.config(show="")
            eye_2.config(text="Hide Password")
        else:
            conf_password.config(show="*")
            eye_2.config(text="Show Password")

    def choseProfile():
        res = filedialog.askopenfile(mode="r", filetypes =[('JPEG', '.jpg'),
                                ('GIF', '.gif'),
                                ('PNG', '.png'),])
        if res.name:
            image = ImageTk.PhotoImage(Image.open(res.name))
            print(image)

    Label(window, image=logo).grid(
        row=0, column=0, columnspan=3
    )
    Label(window, text="Register Form", font=("Arial", 12, "bold")).grid(
        row=1, column=0, columnspan=3
    )
    Label(window, text="Username", font=("Arial", 12)).grid(
        row=2, column=0, sticky=W, pady=5, padx=15
    )
    Label(window, text="Password", font=("Arial", 12)).grid(
        row=3, column=0, sticky=W, pady=5, padx=15
    )
    Label(window, text="Confirm password", font=("Arial", 12)).grid(
        row=4, column=0, sticky=W, pady=5, padx=15
    )

    pass_ey_1 = BooleanVar()
    pass_ey_2 = BooleanVar()

    username = Entry(window, font=("Arial", 12))
    username.grid(row=2, column=1, sticky=W)
    password = Entry(window, font=("Arial", 12), show='*')
    password.grid(row=3, column=1, sticky=W)
    conf_password = Entry(window, font=("Arial", 12), show='*')
    conf_password.grid(row=4, column=1, sticky=W)
    error = Label(window, text="", fg="red", font=("Arial", 11, "italic"))
    error.grid(row=5, column=1)
    eye_1 = Checkbutton(window, text="Show Password",
                      font=("Arial", 12),
                      variable=pass_ey_1, command=hide_show_1, onvalue=True, offvalue=False)
    eye_1.grid(row=3, column=2)

    eye_2 = Checkbutton(window, text="Show Password",
                      font=("Arial", 12),
                      variable=pass_ey_2, command=hide_show_2, onvalue=True, offvalue=False)
    eye_2.grid(row=4, column=2)



    frame_1 = Frame(window , height=50, width=w)
    frame_1.grid(row=6, column=0, columnspan=3, pady=5)

    # add an image

    profile_label = Label(frame_1, image=_default_profile)
    profile_label.grid(row=0, column=0)

    Button(frame_1, text="Choose Profile", width=20, bd=5, bg="lightgrey", fg="white",
           command=choseProfile).grid(row=1, column=0, pady=5)
    Label(window, text="Email address", font=("Calibri", 12)).grid(row=7, column=0, sticky=W, pady=5, padx=15)
    email_address=Entry(window, font=("Calibri",12))
    email_address.grid(row=7,column=1,sticky=W)
    Label(window, text="Identity number", font=("Calibri", 12)).grid(row=8, column=0, sticky=W, pady=5, padx=15)
    i_d=Entry(window, font=("Calibri",12))
    i_d.grid(row=8,column=1,sticky=W)
    Label(window, text="Nationality", font=("Calibri", 12)).grid(row=9, column=0, sticky=W, pady=5, padx=15)
    Label(window,text="Gender",font=("Calibri",12)).grid(row=11,column=0,sticky=W,pady=5,padx=15)
    Label(window, text="Skills", font=("Calibri", 12)).grid(row=10, column=0, sticky=W, pady=5, padx=15)

    skills_var=StringVar()
    skill_types=["Software developer","Java","AI","ML","Python","C++","C#","C","Javascript","VB"]
    skills_=OptionMenu(window,skills_var,*skill_types)
    skills_.grid(row=10, column=1,pady=5,sticky=W,padx=5)

    natinality_var=StringVar()
    nationalities=["African","Coloured","Idian","Asian","White"]
    nationality=OptionMenu(window,natinality_var,*nationalities)
    nationality.grid(row=9, column=1,pady=5,sticky=W,padx=5)

    gender_var= StringVar()
    genders=["Male","Female","Trans-gender"]
    gender=OptionMenu(window,gender_var,*genders)
    gender.grid(row=11,column=1,pady=5,sticky=W,padx=5)


    Button(window, text="Login", font=("Arial", 12), width=10, bd=5, bg="green",
           fg="white",
           command=lambda: register(username.get(), password.get())
           ).grid(row=12, column=0, pady=10)
    Button(window, text="Register", font=("Arial", 12), width=10,bd=5, bg="orange",
           fg="white").grid(row=12, column=1)
    Button(window, text="Close", font=("Arial", 12), width=10, bd=5, bg="red",
           fg="white", command=close).grid(row=12, column=2)
