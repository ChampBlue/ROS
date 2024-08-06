import rospy
from std_srvs.srv import SetBool, SetBoolResponse

def handle_set_bool(req):
    rospy.loginfo("Request data: %s" % req.data)
    if req.data:
        message = "Received True"
    else:
        message = "Received False"
    response = SetBoolResponse(success=True, message=message)
    return response

def set_bool_server():
    rospy.init_node('set_bool_server')  
    s = rospy.Service('set_bool_service', SetBool, handle_set_bool) 
    rospy.loginfo("SetBool service server ready.")
    rospy.spin() 

if __name__ == "__main__":
    set_bool_server()
