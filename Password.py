#We want to create a console which can perform like a login system.
#We need to insert libs at the beginning as always, otherwise the functions won't work properly
import Tkinter as tk
import sys
import os
failure_max = 5
passwords = [('Imperial', 'is the best')]
#here we use entry instead of pack
def make_entry(root, caption, width=None, **options):
    tk.Label(root, text=caption).pack(side=tk.TOP)
    entry = tk.Entry(root, **options)
    if width:
        entry.config(width=width)
    entry.pack(side=tk.TOP, padx=10, fill=tk.BOTH)
    return entry
#here we can check the password by press the Enter button
def enter(event):
    check_password()
def check_password(failures=[]):
    #check whether the inputs mathch the given value or not.
    if (user.get(), password.get()) in passwords:
        self.destroy()
        print('Logged in')
        os.system('modulefinal.py')
        return
    failures.append(1)
#here we can use an exception, but it will slow down the speed.
    if sum(failures) >= failure_max:
        self.destroy()
        sys.exit('Unable to open')
    else:
        self.title('Try again. Attempt %i/%i' % (sum(failures)+1, failure_max))
#build up a frame and assighn the configuration of it
self = tk.Tk()
self.geometry('300x160')
self.title('Enter Your Information')
root = tk.Frame(self, padx=10, pady=10)
root.pack(fill=tk.BOTH, expand=True)
#follow by show'*' which make sure passoword won't be shown.
user = make_entry(root, "User name:", 16)
password = make_entry(root, "Password:", 16, show="*")
#create a button in widget which act as a "start'
b = tk.Button(root, borderwidth=4, text="Login", width=10, pady=8, command=check_password,activebackground='yellow')
b.pack(side=tk.BOTTOM)
password.bind('<Return>', enter)
#Moving fouces to a widget
user.focus_set()
root.mainloop()