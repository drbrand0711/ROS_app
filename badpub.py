#!/usr/bin/env python3
import rospy
import numpy as np
import random
from ros_abhiyaan.msg import CheckedData

def badpub():
    data = CheckedData()
    rate = rospy.Rate(0.5)
    while not rospy.is_shutdown():
        data.rx = [random.randint(0,256) for i in range(5)]
        data.checksum = 0
        rospy.loginfo(data)
        pub.publish(data)
        rate.sleep()
if __name__ == '__main__':
    try:
        rospy.init_node('badpub',anonymous = True)
        pub = rospy.Publisher('rx_msgs',CheckedData,queue_size=10)
        badpub()
    except rospy.ROSInterruptException:
        pass
