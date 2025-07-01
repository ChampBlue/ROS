# 우분투 설치
1. rasberrypi imager로 ubuntu20.04.5 LTS 설치

# 우분투 서버에서 와이파이 설정
- sudo nano /etc/netplan/50-cloud-init.yaml

network:
  version: 2
  renderer: networkd   <- renderer: NetworkManger로 하면 nmcli device wifi rescan 명령어 먹음

  ethernets:
    eth0:
      dhcp4: true
      optional: true

  version: 2
  wifis:
    wlan0:
      dhcp4: true
      dhcp6: yes
      optional: true         # 부팅 시 와이파이 없어도 부팅 계속
      access-points:
        "YOUR_SSID":         # 여기에 사용하시는 와이파이 이름(SSID)
          password: "YOUR_PASSWORD"

- sudo netplan try
-> 문제 없으면 apply? 물음 -> enter로 확정
- 또는 그냥 sudo netplan apply 바로 입력

# 우분투 비번, id 변경
1. 비번 
  1) sudo nano /etc/pam.d/common-password
  -> # here are the per-package modules (the "Primary" block)
  password        [success=1 default=ignore]      pam_unix.so sha512 minlen=2

  2) passwd 

2. id(pi 아이디 만든다는 예시)
  1) sudo adduser pi
      -> Enter the new value, or press Enter for the default
      Full Name []:
    다 enter치면됨

  2) sudo usermod -aG sudo pi

  3) su - pi

  4) reboot

  5) ssh pi@ ~ 접속

  6) sudo pkill -u ubuntu

  7) sudo deluser --remove-home ubuntu

  8) sudo hostnamectl set-hostname pi
 
  9) sudo sed -i 's/^127\.0\.1\.1\s\+.*/127.0.1.1 pi/' /etc/hosts

    또는
    
    sudo nano /etc/hosts
    -> 127.0.0.1 localhost
    -> 127.0.0.1 pi

  10) 터미널 닫고 재접속 or 재부팅
  -> pi@pi:~$

# ROS2 FOXY설치(PC도 공통)
https://docs.ros.org/en/foxy/Installation/Ubuntu-Install-Debians.html

- SBC는 굳이 DESKTop 말고 sudo apt install ros-foxy-ros-base로 설치