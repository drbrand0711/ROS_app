#!/usr/bin/env python3
import rospy
from ros_abhiyaan.msg import CheckedData
from std_msgs.msg import String
from crc import Calculator,Crc16

def callback(data):
    calculator = Calculator(Crc16.CCITT)
    verified = calculator.verify(data.rx,data.checksum)
    if verified == True:
        msg='OK'
        rospy.loginfo(msg)
        pub.publish(msg)
    else:
        msg = 'Corrupted'
        rospy.loginfo(msg)
        pub.publish(msg)
if __name__ =='__main__':
    try:
        rospy.init_node('verifier',anonymous = True)
        rospy.Subscriber('rx_msgs',CheckedData,callback)
        pub = rospy.Publisher('crc_result',String,queue_size = 10)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
