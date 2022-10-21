from machine import Pin,PWM, I2C #importing PIN and PWM
import time #importing time
import utime
from utime import sleep
import ssd1306
import sh1106

# Defining motor pins
motor1=Pin(8,Pin.OUT)
motor2=Pin(9,Pin.OUT)
motor3=Pin(10,Pin.OUT)
motor4=Pin(11,Pin.OUT)
lampu = Pin(0, Pin.OUT)
# lampu_val = lampu.value(1)


# Defining  right and left IR digital pins as input
right_ir = Pin(2, Pin.IN)
left_ir = Pin(3, Pin.IN)
#define pin oled
sda=machine.Pin(4)
scl=machine.Pin(5)

# default_oled = True
def oled(x,y):
    i2c = I2C(0, scl=scl, sda=sda, freq=400000)

    display = sh1106.SH1106_I2C(128, 64, i2c, Pin(4), 0x3c)
    display.sleep(x)
    lampu_val = lampu.value(y)

    display.fill(0) # clear to black
    display.text('Test 1234567890', 0, 0, 1) # at x=0, y=0, white on black
    # line under title
    display.hline(0, 9, 127, 1)
    # bottom of display
    display.hline(0, 30, 127, 1)
    # left edge
    display.vline(0, 10, 32, 1)
    # right edge
    display.vline(127, 10, 32, 1)

    for i in range(0, 128):
        # box x0, y0, width, height, on
        display.fill_rect(i,10, 10, 10, 1)
        # draw black behind number
        display.fill_rect(10, 21, 30, 8, 0)
        display.text(str(i), 10, 21, 1)
        display.show() # update display
        # utime.sleep(0.001)
    # 
#         print('done')
        
# def oled_off():
#     i2c = I2C(0, scl=scl, sda=sda, freq=400000)
# 
#     display = sh1106.SH1106_I2C(128, 64, i2c, Pin(4), 0x3c)
#     display.sleep(True)
# 
#     display.fill(0) # clear to black
#     display.text('Test 1234567890', 0, 0, 1) # at x=0, y=0, white on black
#     # line under title
#     display.hline(0, 9, 127, 1)
#     # bottom of display
#     display.hline(0, 30, 127, 1)
#     # left edge
#     display.vline(0, 10, 32, 1)
#     # right edge
#     display.vline(127, 10, 32, 1)
# 
#     for i in range(0, 128):
#         # box x0, y0, width, height, on
#         display.fill_rect(i,10, 10, 10, 1)
#         # draw black behind number
#         display.fill_rect(10, 21, 30, 8, 0)
#         display.text(str(i), 10, 21, 1)
#         display.show() # update display
#         # utime.sleep(0.001)
#     # 
#         print('done')
        
        

# sda=machine.Pin(4)
# scl=machine.Pin(5)
# i2c = I2C(0, scl=scl, sda=sda, freq=400000)
# 
# display = sh1106.SH1106_I2C(128, 64, i2c, Pin(4), 0x3c)
# display.sleep(False)
# 
# display.fill(0)
# display.text('CoderDojo', 0, 0, 1)
# display.show()
# 
# print('done')


# Forward
def move_forward():
    motor1.low()
    motor2.high() #high
    motor3.high() #high
    motor4.low()
    
# Backward
def move_backward():
    motor1.high()
    motor2.low()
    motor3.low()
    motor4.high()
    
#Turn Right
def turn_right():
    motor1.low()
    motor2.high()
    motor3.low()
    motor4.high()
    
#Turn Left
def turn_left():
    motor1.high()
    motor2.low()
    motor3.high()
    motor4.low()
   
#Stop
def stop():
    motor1.low()
    motor2.low()
    motor3.low()
    motor4.low()
    

    
while True:
    
    right_val=right_ir.value() #Getting right IR value(0 or 1)
    left_val=left_ir.value() #Getting left IR value(0 or 1)
    
    print(str(right_val)+"-"+str(left_val))
    
    
    
    # Controlling robot direction based on IR value
    if right_val==0 and left_val==0:
        move_forward()
        oled(True, 0)
        
        
    elif right_val==1 and left_val==0:
        turn_right()
        oled(True, 0)
        
    elif right_val==0 and left_val==1:
        turn_left()
        oled(True, 0)
    else:
        stop()
        oled(False, 1)
        
