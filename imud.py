#!/usr/bin/env python
import serial
import time
import rospy
import roslib
from std_msgs.msg import *
from sensor_msgs.msg import *

def talker1():
	pub=rospy.Publisher('/imu/data', Imu, queue_size=12)
	rospy.init_node('data1')
	rate=rospy.Rate(10)
	while not rospy.is_shutdown():
			msg1=Imu()
			msg1.header.stamp=rospy.Time.now()
			msg1.header.frame_id='odom'
			msg1.orientation.x=20.0
			msg1.angular_velocity.y=3.0
			msg1.linear_acceleration.x=1.0
			pub.publish(msg1)
			rate.sleep()
if __name__ == '__main__':
	talker1()
