# ROS NAVIGATION에 대하여...

# 주제
    1. 속도와 가속도
    2. 글로벌 플래너
        - global planner selection
        - global planner parameter
    3. local planner
        - local planner selection
        - DWA Local Planner
            - dwa 알고리즘
            - dwa forward simulation
            - dwa 궤적 점수화
            - 기타 dwa 매개변수
    4. costmap parameters
    5. amcl
    6. recovery behavior
    7. dynamic reconfigure
    8. problems

1. 속도와 가속도
    * 이 섹션은 synchro-drive로봇과 관련됨

    - 로봇의 역학(예: 로봇의 속도 및 가속도)은 동적 창 접근법(DWA) 및 시간 탄성 밴드(TEB)을 포함한 로컬 플래너에 필수적임.

    - ros navigation stack에서 로컬플래너는 오도매트리 메시지("odom" topic)를 받아 들이고 로봇의 움직임을 제어하는 속도 명령("cma_vel" topci)을 출력함.

    - Max/min velocity(최대/최소 속도)와 acceleration(가속도)는 mobile base의 두가지 기본 매개 변수임.

    -  