import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3

def callback(data):
    # 수신된 Twist 메시지를 로그로 출력합니다.
    rospy.loginfo("Received cmd_vel: linear=%s angular=%s", data.linear, data.angular)
    
    # 로봇의 속도를 설정하는 로직을 여기에 추가할 수 있습니다.
    # 터틀봇의 실제 속도 제어는 로봇의 하드웨어와 연결된 드라이버가 처리합니다.

def listener():
    # 'turtlebot_subscriber'라는 이름의 ROS 노드를 초기화합니다.
    rospy.init_node('turtlebot_subscriber', anonymous=True)
    
    # '/cmd_vel' 토픽을 구독하는 서브스크라이버를 생성합니다.
    # 구독한 메시지가 도착하면 callback 함수를 호출합니다.
    rospy.Subscriber('/cmd_vel', Twist, callback)
    
    # 노드가 종료될 때까지 지속적으로 콜백 함수를 호출하며 대기합니다.
    rospy.spin()

if __name__ == '__main__':
    # 메인 함수가 실행될 때 listener 함수를 호출하여 노드를 시작합니다.
    listener()
