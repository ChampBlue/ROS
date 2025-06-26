import rospy
from std_msgs.msg import String

#chatter 토픽에서 메시지를 받을때 호출되는 콜백 함수
def callback(data):
    rospy.loginfo("I heard %s", data.data)

def listener():
    rospy.init_node('listener', anonymous=True)     
    #lister라는 이름의 ros노드를 초기화
    #anonymous = True로 설정해 동일한 이름의 노드가 여러개 실행될 수 있도록 설정
    
    rospy.Subscriber('chatter', String, callback) 
    #chatter 토픽을 구독하는 서브스크라이버를 생성함.
    #구독한 메시지가 도착하면 callback 함수를 호출
    
    rospy.spin()
    #노드가 종료될때 까지 지속적으로 콜백 함수를 호출하며 대기함.

if __name__ == '__main__':
    listener()
