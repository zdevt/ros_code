#!/usr/bin/env python
#-*- coding:utf-8 -*-
#       FileName:  listener.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-05-21 11:10:54
#  Last Modified:  2018-05-22 08:52:47
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:


import rospy 
from std_msgs.msg import String 

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("chatter",String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
