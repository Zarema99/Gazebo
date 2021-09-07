#!/usr/bin/env python

#data are published to joint4
#data are specified by a user through input( )
#it is supposed that the user provides adequate data
#the range of joint position is [-2, 2]

import rospy
from std_msgs.msg import Float64

def publish_to_joint4():
    pub = rospy.Publisher('/robot/joint4_position_controller/command', Float64, queue_size = 10)
    rospy.init_node('publish_to_joint4', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    data = input("Please provide data: ")
    rospy.loginfo(data)
    pub.publish(data)
    while not rospy.is_shutdown():
        data2 = input("Please provide new data: ")
	if data2 < data:
		rospy.loginfo(data2)
		pub.publish(data2)
		data = data2
		rate.sleep()
        else:
		print('Invalid data. Data should be smaller than %.2f' %data)
                        

if __name__ == '__main__':
    try:
        publish_to_joint4()
    except rospy.ROSInterruptException:
        pass
