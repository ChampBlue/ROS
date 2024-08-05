import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3

def callback(data):
    rospy.loginfo("Received cmd_vel: linear=%s angular=%s", data.linear, data.angular)
    
def listener():
    rospy.init_node('turtlebot_subscriber', anonymous=True)
    rospy.Subscriber('/cmd_vel', Twist, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
