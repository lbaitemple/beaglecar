#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from simple_motor.srv  import *
from std_msgs.msg import Float32
from std_msgs.msg import String
import settings
from settings import wiringport
import os,sys, select, termios, tty
import json
import time

# Import the PCA9685 module.
#This is for REV 2.2
# import Adafruit_PCA9685

# Initialise the PCA9685 using the default address (0x40).
#pwm = Adafruit_PCA9685.PCA9685(0x40)

# pwm.set_pwm_freq(92.7)

s0 = wiringport[settings.PINS['servo0']]
s1 = wiringport[settings.PINS['servo1']]

cmd= ["gpio mode {} pwm".format(s0),
     "gpio mode {} pwm".format(s1),
     "gpio pwm-ms",
     "gpio pwmc 1920",
     "gpio pwmr 100",
 ]

def set_car(req):
#    set(12, req.speed)
#    set(13, req.turn)
    print(req.speed, req.turn)

def setspeed(pin, sped):
    if (pin==12):
        str="gpio pwm {} {}".format(s0, sped*100)
        os.system(str)
    elif (pin==13):
        str="gpio pwm {} {}".format(s1, sped*100)
        os.system(str)

#def on_new_twist(data):
#    pwm.set_pwm(8, 0, int(data.linear.x))
#    print("This is Motor values" , data.linear.x)
#    setspeed(12, data.linear.x)
#    print("This is servo values" , data.angular.x)
#    setspeed(13, data.angular.x)

#def on_new_servo(data):
#    pwm.set_pwm(9, 0, int(data.data))
#    setspeed(13, data.data)

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener')
    #subscriber_twist = rospy.Subscriber("cmd_vel", Twist, on_new_twist, queue_size=10)
    s = rospy.Service('drive_car', Drive, set_car)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()

