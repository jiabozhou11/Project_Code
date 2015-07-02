import pyb
from pyb import Pin, Timer
from finalchannel1 import value1, value2, value3, value4
# create a suqare wave with modified dutycycle and frequency.
def f():
    #Led 1 here performed as an indicator.
    pyb.LED(1).toggle()
    ch = Timer(2, freq=1/float(value1)).channel(10*float(value4), Timer.PWM, pin=Pin('X3'))
    ch.pulse_width_percent(float(value3)/(float(value2)+float(value3)))
#use swich button to initiate a function(f).
sw = pyb.Switch()
sw.callback(f)