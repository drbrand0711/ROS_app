#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import Int32
import random

def talker():
    pub = rospy.Publisher('readings', Int32, queue_size=10)
    rospy.init_node('sender', anonymous=True)
    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():
        rint = random.choice([-1,1])
        rospy.loginfo(rint)
        pub.publish(rint)
        rate.sleep()
  
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
