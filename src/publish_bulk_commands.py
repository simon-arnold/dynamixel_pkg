#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32MultiArray 
from dynamixel_sdk_examples.msg import SetPosition 


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard")
    

    
    

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("motor/position", Int32MultiArray, callback)
    
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
   set_position_pub =rospy.Publisher("set_position", SetPosition, queue_size=10)
   listener()
    


