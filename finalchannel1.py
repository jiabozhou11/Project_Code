from Tkinter import * # get base widget set
from dialogTable import demos # button callback handlers
from Quitter import Exit # attach a quit frame to me
import tkSimpleDialog
from scipy import signal
from drawnow import drawnow
import matplotlib.pyplot as plt
import numpy as np
import time
from Tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
#before this time, i want to build up a dynamic system.
#but i found that you need to restart the pyboard to load the new program when you change the value in your code.
plt.ion()
class Demo(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.grid()
        OPTIONS = [
        "x0.01",
        "x0.1",
        "x1",
        "x10",
        "x100",
        "x1000"
        ]
        #set the initial values.
        variable1 = StringVar(self)
        variable1.set(OPTIONS[2]) # default value
        variable2 = StringVar(self)
        variable2.set(OPTIONS[2]) # default value
        variable3 = StringVar(self)
        variable3.set(OPTIONS[2]) # default value
        variable4 = StringVar(self)
        variable4.set(OPTIONS[3]) # default value
        #set up configurations of widget
        Label(self, text="S1 Rate (PPS) ").grid(row=0)
        Menu1=apply(OptionMenu, (self,variable1 ) + tuple(OPTIONS))
        Menu1.grid(row=0, column=1,columnspan ='20')
        Menu1.configure(bg = 'white')
        self.var = IntVar()
        yourscale1=Scale(self, command=self.Move1,from_=1, to=10,orient=HORIZONTAL,length=500,tickinterval=0.5, resolution=0.1, cursor = 'hand2 ',background='white',troughcolor='white')
        yourscale1.grid(columnspan ='200',rowspan = '4')
        yourscale1.set(2)
        Label(self, text="S1 Delay (MS)").grid(row=5, column ='0')

        apply(OptionMenu, (self,variable2 ) + tuple(OPTIONS)).grid(row=5, column=1,columnspan ='20')
        yourscale2=Scale(self, command=self.Move2,from_=1, to=10,orient=HORIZONTAL,length=500,tickinterval=0.5, resolution=0.1, cursor = 'hand2 ',background='white',troughcolor='white')
        yourscale2.grid(columnspan ='200',rowspan = '4')
        yourscale2.set(2)
        Label(self, text="S1 Duration (MS)").grid(row=10, column ='0')
        apply(OptionMenu, (self,variable3 ) + tuple(OPTIONS)).grid(row=10, column=1,columnspan ='20')
        yourscale3=Scale(self,command=self.Move3,from_=1, to=10,orient=HORIZONTAL,length=500,tickinterval=0.5, resolution=0.1, cursor = 'hand2 ',background='white',troughcolor='white')
        yourscale3.grid(columnspan ='200',rowspan = '4')
        yourscale3.set(10)
        Label(self, text="S1 Volts").grid(row=15, column ='0')
        apply(OptionMenu, (self,variable4 ) + tuple(OPTIONS)).grid(row=15, column=1,columnspan ='20')
        yourscale4=Scale(self,command=self.Move4, from_=1, to=15,orient=HORIZONTAL,length=500,tickinterval=1, resolution=0.1, cursor = 'hand2 ',background='white',troughcolor='white')
        yourscale4.grid(columnspan ='100',rowspan = '4')
        yourscale4.set(10)
        Button(self, text="Start", command=self.onRun,height =1, width = 10).grid(row =20,pady=3)
        Exit(self).grid(row =20, column=96,columnspan=10)
        return
    #we need to save the value for furture use.
    def Move1(self, value):
        global value1
        value1 = DoubleVar()
        value1 = value
        print 'The value of rate changed to', value
    def Move2(self, value):
        global value2
        value2 = DoubleVar()
        value2 = value
        print 'The value of delay changed to', value
    def Move3(self, value):
        global value3
        value3 = DoubleVar()
        value3 = value
        print 'The value of duration changed to', value
    def Move4(self, value):
        global value4
        value4 = DoubleVar()
        value4 = value
        print 'The value of voltage changed to', value
    #Once you press the start button, a new widget should arise.
    def onRun(self):
        #limit = int(raw_input('Enter the time range :'))
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.grid()
        ax.set_ylim(-(10*float(value4)+10), 10*float(value4)+10)
        ax.set_xlim(0,20)
        ax.set_ylabel('Voltage(V)')
        ax.set_xlabel('Time(MS)')
        ax.set_title('Channel 1')
        t = np.linspace(0, 20, 500, endpoint=False)
        plt.plot(t, 10*float(value4)*signal.square(2 * np.pi /float(value1) * t,duty=float(value3)/(float(value2)+float(value3))))
#create the background console.
self1 = Tk()
self1.geometry('510x460')
self1.title('Simulator Channel 1')
self1.tk_setPalette(background='white', foreground='black', activeBackground='white', activeForeground='black')
if __name__ == '__main__':
    print demos.keys()
    Demo().mainloop()