# CamJam EduKit 3 - Robotics

import time # Import the Time library
from gpiozero import Robot, LED

# Set up a robot on pins 7, 8, 9, 10
bot = Robot(left=(7, 8), right=(9, 10))

bot.stop()
import sys, termios, tty, os

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

PIN_LED = 25
myled = LED(PIN_LED)
button_delay = 0.2

for x in range(0,3):
    myled.on()
    time.sleep(0.25)
    myled.off()
    time.sleep(0.25)

while True:
    char = getch()

    if (char == "q"):
        bot.stop()
        exit(0)  

    if (char == "a"):
        print('Left pressed')
        bot.left()
        time.sleep(button_delay)

    if (char == "d"):
        print('Right pressed')
        bot.right()
        time.sleep(button_delay)          

    elif (char == "w"):
        print('Up pressed')
        bot.forward()
        time.sleep(button_delay)          
    
    elif (char == "s"):
        print('Down pressed')    
        bot.backward()
        time.sleep(button_delay)  
    
    bot.stop()