

from tkinter import *
from tkinter import messagebox
from login import login_form
from register import register_form
from state import GlobalState
from PIL import ImageTk, Image

state = GlobalState()

# image
window = Tk()
# overiding the close
window.protocol('WM_DELETE_WINDOW', lambda: close())
# setting the properties of the window
window.title("User Information")
# --------------
w = 400
h = 340
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
position_from_top = int(screen_height/2 - h/2)
position_from_right = int(screen_width/2 - w/2)
window.geometry("{}x{}+{}+{}".format(w, h, position_from_right, position_from_top))

window.resizable(False, False)
window.iconbitmap('./reserved/icon.ico')
_default_profile = ImageTk.PhotoImage(Image.open('./reserved/default.jpg').resize((100, 100)))
logo = ImageTk.PhotoImage(Image.open('./reserved/astro.jpg').resize((100, 100)))

# login
def _login():
    if not state.getOpen():
        _login_form = Toplevel()
        login_form(_login_form, window, state, logo)
        state.setOpen(True)
    else:
        pass

def _register():
    if not state.getOpen():
        _register_form = Toplevel()
        register_form(_register_form, window, state, logo, _default_profile)
        state.setOpen(True)
    else:
        pass
# closing the window
def close():
    response = messagebox.askyesnocancel("Close App", "Are you sure you want to close this app?")
    if response == True:
        window.destroy()
    else:
        window.focus()

Label(window, image=logo).grid(
    row=0, column=0, columnspan=3
)
Label(window, text="Welcome to Our Application", font=("Arial", 12, "bold"), width=40).grid(
    row=1, column=0, columnspan=3
)

Label(window, text="Already Have an Account?", font=("Arial", 8), fg="gray").grid(
    row=2, column=0, columnspan=3, pady=5
)
Button(window, text="Login", font=("Arial", 12), width=10, bd=5, bg="green",
       fg="white", command=_login
       ).grid(row=3, column=1)
Label(window, text="New To this Application?", font=("Arial", 8), fg="gray").grid(
    row=4, column=0, columnspan=3, pady=5
)
Button(window, text="Register", font=("Arial", 12), width=10, bd=5, bg="orange",
       fg="white", command=_register).grid(row=5, column=1)
Label(window, text="Not Interested in this App?", font=("Arial", 8), fg="gray").grid(
    row=6, column=0, columnspan=3, pady=5
)
Button(window, text="Close", font=("Arial", 12), width=10, bd=5, bg="red",
       fg="white", command=close).grid(row=7, column=1)
window.mainloop(0)