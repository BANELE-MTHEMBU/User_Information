# Authentication_form
This is my application for allowing the user to register his or her credentials, if he or she is interested to register, Also allows the user to
log in if he/she already has an account. If the user is not interested he or she is allowed to close the application.

#### Here is the snapshot of my application

````py
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
````