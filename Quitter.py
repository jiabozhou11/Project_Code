from Tkinter import * # get widget classes
from tkMessageBox import askokcancel # get canned std dialog
import sys
class Exit(Frame): # subclass our GUI
    def __init__(self, parent=None): # constructor method
        Frame.__init__(self, parent)
        self.pack()
        button = Button(self, text='Quit', command=self.quit,height = 1, width = 8)
        button.pack(side=LEFT)
    def quit(self):
        ans = askokcancel('Verify exit', "Are you sure?")
        if ans:
            #.destroy() means termiante the whold program.
            self.destroy()

if __name__ == '__main__':
    Exit().mainloop()