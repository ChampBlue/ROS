import rospy
from std_srvs.srv import SetBool, SetBoolResponse
#std_srvs.srv
# ros에서 제공하는 표준 서비스 타입.
    
    # Empty
        # 데이터가 없는 요청 및 응답.
    
    # Trigger 
        # 요청 데이터가 없으며, 응답으로 성공여부와 메시지를 반환.
    
    # SetBool
        # 요청 데이터로 불 값을 받고, 응답으로 성고 여부와 메시지를 반환.
        
def handle_set_bool(req):
    # req : 서비스 요청 객체. 여기선 SetBoolRequest 타입이며, data라는 불 필드를 포함함. 
    #       클라이언트가 보내는 요청 데이터가 이 객체에 포함됨.        
    
    rospy.loginfo("Request data: %s" % req.data)
    
    if req.data:
        message = "Received True"
    else:
        message = "Received False"
    '''
        요청 데이터(req.data)가 true인지 false인지에 따라 다른 응답 메시지를 생성함.
    '''    
    response = SetBoolResponse(success=True, message=message)
    
    return response
    # 생성된 응답 객체를 반환하여 클라이언트에 응답을 보냄
    
def set_bool_server():
    rospy.init_node('set_bool_server')  
    
    s = rospy.Service('set_bool_service', SetBool, handle_set_bool) 
    ''' 
    rospy.Service(name, service_class, handler)
        1. name
            - 서비스 이름을 지정함.
            - 이 이름을 통해 클라이언트가 서비스를 요청할 수 있음.
            
        2. service_class
            - 서비스의 타입을 지정함. 여기서는 std_srvs.srv.SetBool 타입을 사용함.
        
        3. handler 
            - 서비스 요청을 처리할 콜백함수를 지정함. 이 함수는 서비스 요청이 들어올 때 마다 호출됨.
            - 콜백함수는 요청 객체를 매개변수로 받아 응답 객체를 반환해야함. 
    
        4. 반환값
            - service : 생성된 서비스 객체를 반환함.
    '''    
        
    rospy.loginfo("SetBool service server ready.")
    rospy.spin() 

if __name__ == "__main__":
    set_bool_server()