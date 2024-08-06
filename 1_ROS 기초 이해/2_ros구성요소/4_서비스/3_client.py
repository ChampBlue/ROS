import rospy
from std_srvs.srv import SetBool, SetBoolRequest

def set_bool_client(data):
    rospy.wait_for_service('set_bool_service')  
    try:
        set_bool_service = rospy.ServiceProxy('set_bool_service', SetBool)  
        request = SetBoolRequest(data=data)  
        response = set_bool_service(request)  
        rospy.loginfo("Service call succeeded: %s" % response.message)
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s" % e)

if __name__ == "__main__":
    rospy.init_node('set_bool_client') 
    set_bool_client(True)  
    set_bool_client(False)  
