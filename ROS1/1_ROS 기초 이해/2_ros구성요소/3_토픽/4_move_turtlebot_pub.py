import rospy
from geometry_msgs.msg import Twist
import time

def move_turtlebot():
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.init_node('turtlebot_mover', anonymous=True)
    rate = rospy.Rate(10)  # 10 Hz

    move_cmd = Twist()

    # 10% 속도로 앞으로 이동 (3초)
    move_cmd.linear.x = 0.1  # 앞쪽으로 10% 속도
    move_cmd.angular.z = 0  # 회전 없음
    rospy.loginfo("Moving forward")
    for _ in range(30):  # 3초 동안 (10 Hz * 3초 = 30회)
        pub.publish(move_cmd)
        rate.sleep()

    # 멈춤 (1초)
    move_cmd.linear.x = 0
    rospy.loginfo("Stopping")
    for _ in range(10):  # 1초 동안 (10 Hz * 1초 = 10회)
        pub.publish(move_cmd)
        rate.sleep()

    # 10% 속도로 뒤로 이동 (3초)
    move_cmd.linear.x = -0.1  # 뒤쪽으로 10% 속도
    rospy.loginfo("Moving backward")
    for _ in range(30):  # 3초 동안 (10 Hz * 3초 = 30회)
        pub.publish(move_cmd)
        rate.sleep()

    # 멈춤 (1초)
    move_cmd.linear.x = 0
    rospy.loginfo("Stopping")
    for _ in range(10):  # 1초 동안 (10 Hz * 1초 = 10회)
        pub.publish(move_cmd)
        rate.sleep()

if __name__ == '__main__':
    try:
        move_turtlebot()
    except rospy.ROSInterruptException:
        pass
