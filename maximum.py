#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
from std_msgs.msg import String
max = -100
state = False
msg = 'no'
def callback(data):
    global max
    global state
    new = data.data
    if new > max:
        max = new
        msg = f"A new record! {max}"
        rospy.loginfo(msg)
        pub.publish(msg)
        state = True
        rospy.logerr("I got here!")
    else:
        state = False
def maximum():
    global state
    rospy.spin()
if __name__ == '__main__':
    try:
        rospy.init_node('maximum' , anonymous = True)
        rospy.Subscriber("distance" , Int32 , callback)
        pub = rospy.Publisher('message' , String , queue_size = 10)
        maximum()
    except rospy.ROSInterruptException:
    	
        pass
        
