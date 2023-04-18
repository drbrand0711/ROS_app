#!/usr/bin/env python3
import rospy
import numpy as np
import random
from ros_abhiyaan.msg import CheckedData
from crc import Calculator, Crc16

def goodpub():
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        data = CheckedData()
        data.rx = [random.randint(0,256) for i in range(5)]
    
        data.checksum =Calculator(Crc16.CCITT).checksum(bytes(data.rx)) 
        rospy.loginfo(data)
        pub.publish(data)
        rate.sleep()
    

if __name__ == '__main__':
    try:
        rospy.init_node('goodpub',anonymous = True)
        pub = rospy.Publisher("gp",CheckedData,queue_size = 10)
        goodpub()
        
    except rospy.ROSInterruptException:
        pass
