import rospy   
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10) 
    rospy.init_node('talker', anonymous=True) 
    rate = rospy.Rate(10)       
    
    for i in range(5):
        hello_str = f"hello world{rospy.get_time()}"
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()    
    
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass