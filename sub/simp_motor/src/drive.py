#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32
from std_msgs.msg import String
# Import the PCA9685 module.
import Adafruit_PCA9685

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685(0x40)

pwm.set_pwm_freq(92.7)

def setspeed( pin, sped):
    pos = int(sped*4096)
    print(pos)
    pwm.set_pwm(pin, 0, pos)

def on_new_twist(data):
#    pwm.set_pwm(8, 0, int(data.linear.x))
    setspeed(8, data.linear.x)
    setspeed(9, data.angular.x )

def on_new_servo(data):
#    pwm.set_pwm(9, 0, int(data.data))
    setspeed(9, data.data)

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)
    subscriber_twist = rospy.Subscriber("cmd_vel", Twist, on_new_twist, queue_size=10)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
