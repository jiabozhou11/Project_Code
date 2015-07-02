#since we have imported pyb in boot.py, we dont need to do this again.
accel = pyb.Accel()
light = pyb.LED(3)
#set up the limitation (when the pyboard vibrate too much, a led should indicate this).
SENSITIVITY = 3
#keep running the loop
while True:
    x = accel.x()
    if abs(x) > SENSITIVITY:
        light.on()
    else:
        light.off()
    pyb.delay(100)