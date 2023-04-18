#!/usr/bin/env python3
import rospy
from std_msgs.msg import  Int32

sum =0
def callback(data):
    global sum
    sum = sum + data.data
def integrator():
    
    rospy.init_node('integrator', anonymous = True)
    rospy.Subscriber("readings" , Int32,callback)
    pub = rospy.Publisher('distance' , Int32 , queue_size = 10)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        rospy.loginfo(sum)
        pub.publish(sum)
        rate.sleep()

if __name__ == '__main__':
    try:
        integrator()
    except rospy.ROSInterruptException:
        pass
