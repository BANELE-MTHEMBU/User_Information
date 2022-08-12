from tkinter import *
from tkinter import messagebox

def login_form(window, mainWindow, state, logo):
    """
    :param window: this is the top level window for the logn form
    :param mainWindow: this is the welcome page
    :return:
    """
    window.resizable(False, False)
    # setting the properties of the window
    window.title("Login")
    # --------------
    w = 400
    h = 300
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    position_from_top = int(screen_height / 2 - h / 2)
    position_from_right = int(screen_width / 2 - w / 2)
    window.geometry("{}x{}+{}+{}".format(w, h, position_from_right, position_from_top))

    username_1 = "username"
    password_1 = "password"
    # ---------
    window.resizable(False, False)
    window.iconbitmap('./reserved/icon.ico')
    window.protocol('WM_DELETE_WINDOW', lambda: close())
    # login
    def login(username: str, password: str):
        # ' useRname    ' -> ' username    ' -> 'username'
        if username.lower().strip() == username_1 and password == password_1:
            # open main app
            error.config(text="")
            messagebox.showinfo("App", "You are logged in.")
        else:
            error.config(text="Invalid credentials.")


    # closing the window
    def close():
        res = messagebox.askyesnocancel("Close Login Form", "Are you sure you want to close this login form?")
        if res == True:
            state.setOpen(False)
            window.destroy()
        else:
            window.focus()
    # hiding and showing passwords
    def hide_show():
        if pass_ey.get() == True:
            password.config(show="")
            eye.config(text="Hide Password")
        else:
            password.config(show="*")
            eye.config(text="Show Password")


    Label(window, image=logo).grid(
        row=0, column=0, columnspan=3
    )
    Label(window, text="Login Form", font=("Arial", 12, "bold")).grid(
        row=1, column=0, columnspan=3
    )
    Label(window, text="username", font=("Arial", 12)).grid(
        row=2, column=0, sticky=W, pady=5, padx=15
    )
    Label(window, text="password", font=("Arial", 12)).grid(
        row=3, column=0, sticky=W, pady=5, padx=15
    )

    pass_ey = BooleanVar()

    username = Entry(window, font=("Arial", 12))
    username.grid(row=2, column=1, sticky=W)
    password = Entry(window, font=("Arial", 12), show='*')
    password.grid(row=3, column=1, sticky=W)
    error = Label(window, text="", fg="red", font=("Arial", 11, "italic"))
    error.grid(row=4, column=1)
    eye = Checkbutton(window, text="Show Password",
                      font=("Arial", 12),
                      variable=pass_ey, command=hide_show, onvalue=True, offvalue=False)
    eye.grid(row=5, column=1)

    Button(window, text="Login", font=("Arial", 12), width=10, bd=5, bg="green",
           fg="white",
           command=lambda: login(username.get(), password.get())
           ).grid(row=6, column=0, pady=10)
    Button(window, text="Register", font=("Arial", 12), width=10, bd=5, bg="orange",
           fg="white").grid(row=6, column=1)
    Button(window, text="Close", font=("Arial", 12), width=10, bd=5, bg="red",
           fg="white", command=close).grid(row=6, column=2)