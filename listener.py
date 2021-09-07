#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %.2f', data.data)

def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('/robot/joint4_position_controller/command', Float64, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
