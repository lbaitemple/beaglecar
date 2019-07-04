#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32
from sensor_msgs.msg import Joy
from std_msgs.msg import String
import settings
from suiron import SuironIO
from suiron import Clock
from settings import wiringport
import os,sys, select, termios, tty
import json
import time
import Adafruit_PCA9685

#---------------------------------------------------------------
#Set your parameters max speeds forward(maxspeed) and backwards(minspeed) car freq and sensor address
maxspeed = 0.17
minspeed = 0.13
carFreq = 97.1 # CHECK YOUR BOARD AGAINST OSCILLOSCOPE AND MAKE SURE IT IS AS CLOSE TO 100Hz
address = 0x40 # default is 0x40
#-------------------------------------------------------------
#-----------------------------------------------------------------
REV = 2.3 # select your board
# If your board has a PWM module built in we will need the correct chip
if REV == 2.3:
#    import Adafruit_PCA9685
# Initialise the PCA9685 using the default address (0x40).
    pwm = Adafruit_PCA9685.PCA9685(address)
    pwm.set_pwm_freq(carFreq) #CHECK THE PWM OF YOUR BOARD AND FINE TUNE THIS #
#-------------------------------------------------------------

##
#declare io
with open('/home/ubuntu/catkin_ws/settings.json') as d:
    SETTINGS = json.load(d)

print(SETTINGS['width'], SETTINGS['height'])

suironio = SuironIO(id=0, width=SETTINGS['width'], height=SETTINGS['height'], depth=SETTINGS['depth'])
suironio.init_saving()
clck=Clock(suironio, 1000)
clck.start()
#clck.join()

#Our attempt to speed up the process
nos = os.system

if REV == 2.2:
    s0 = wiringport[settings.PINS['servo0']]
    s1 = wiringport[settings.PINS['servo1']]
    cmd= ["gpio mode {} pwm".format(s0),
         "gpio mode {} pwm".format(s1),
         "gpio pwm-ms",
         "gpio pwmc 1920",
         "gpio pwmr 100", ]


def setspeed22(pin, sped):

    if (pin==12):
        str="gpio pwm {} {}".format(s0, sped*100)
        nos(str)
    elif (pin==13):
        str="gpio pwm {} {}".format(s1, sped*100)
        nos(str)

def setspeed23(pin, sped):
    pos = int(sped*4096)
    print(pos)
    pwm.set_pwm(pin, 0, pos)

def callback(data):
#    if data.buttons[4] == 1:
#        maxspeed = maxspeed - 0.01
#        print("your max speed is ",maxspeed)
#    if data.buttons[5] == 1:
#        maxspeed = maxspeed + 0.01
#        print("your max speed is ", maxspeed)
    status={}
    turn = abs(0.05*data.axes[0]-0.15)
    speed  = 0.05*data.axes[1]+0.15
    pwm.set_pwm(8, 0, int(speed))
    status['motor']=0.1
    status['servo']=0.2
    suironio.record_inputs(status)
    if speed > maxspeed:
        speed = maxspeed
    elif speed < minspeed:
        speed = minspeed
    if data.buttons[0] == 1:
        speed = 0.15
        turn = 0.15
        print("You are braking !!")
    if REV == 2.2:
        print("This is Motor values" , speed)
        setspeed22(12, speed)
        print("This is servo values" , turn)
        setspeed22(13, turn)
    elif REV == 2.3:
        print("This is Motor values for 2.3" , speed)
        setspeed23(8, speed)
        print("This is Motor values for 2.3" , turn)
        setspeed23(9,turn)
#    pub.publish(twist)
#    rate.sleep()

def listener():
    rospy.init_node('motor_car', anonymous=True)
    rospy.Subscriber("joy", Joy, callback)
    rospy.spin()    # spin() simply keeps python from exiting until this node is stopped


#START

REV == 2.3
if __name__ == '__main__':
    if REV == 2.2:
        for i in range(0, len(cmd)):
            nos(cmd[i])
            print(cmd[i])
    print(sys.version)
    try:
        listener()
    except KeyboardInterrupt:
        print('Saving file...')

    print('saved;')
    suironio.save_inputs()
    clck.stop()



