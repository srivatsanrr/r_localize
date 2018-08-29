#!/usr/bin/env python
import serial
import time
import rospy
import roslib
from std_msgs.msg import *
from nav_msgs.msg import *
from geometry_msgs.msg import *

def talker():
	pub=rospy.Publisher('/example/odom', Odometry, queue_size=12)
	rospy.init_node('data')
	rate=rospy.Rate(10)
	while not rospy.is_shutdown():
			msg=Odometry()
			msg.header.stamp=rospy.Time.now()
			msg.header.frame_id='odom'
			msg.child_frame_id='base_link'
			msg.twist.twist.linear.x =20.0
			msg.twist.twist.angular.z=5.0
			msg.pose.pose.position.x=10.0
			msg.pose.pose.position.y=1.0
			pub.publish(msg)
			rate.sleep()
if __name__ == '__main__':
	talker()
