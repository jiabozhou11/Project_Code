from Tkinter import * # get base widget set
from dialogTable import demos # button callback handlers (it was my old idea, I keep it for furture use)
from Quitter import Exit # attach a quit frame to me
import os #call another script.
class Demo(Frame):
    #this is the initial function, we combine it with another function by a 'command'
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        Label(self, text="Choose Channel Number").pack()
        self.var = IntVar()
        #here the command is onMove
        Scale(self,command=self.onMove,from_=1, to=2,length=200, ).pack()
        Exit(self).pack(side=RIGHT)
        Button(self, text="Switch", command=self.onRun,height = 1, width = 8).pack(side=LEFT)
    #print the result on the screen to check whether we have switch to the channel we wanted
    def onMove(self, value):
        print 'Switch to channel', value
    #the position is starting from 1. becareful.
    def onRun(self):
        pos = self.var.get()
        if pos == 0:
            print 'You have switched to channel', pos+1
            #how to connect this script with another one.
            os.system('finalchannel1.py')
        elif pos == 1:
            print 'You have switched to channel', pos+1
            os.system('finalchannel2.py')
        print pos
#creat a widget, and modify its configurations.
self1 = Tk()
self1.geometry('300x300')
self1.title('Channel Selection')
self1.tk_setPalette(background='white', foreground='black', activeBackground='white', activeForeground='black')
#here is a normal if function, it will run the loop when you start this program.
if __name__ == '__main__':
    print demos.keys()
    Demo().mainloop()