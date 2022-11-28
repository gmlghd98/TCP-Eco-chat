import json
from socket import *

serverName = '172.23.199.194' # 현재 사용자의 컴퓨터의 IP 주소를 입력해준다.
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
username = input('Input user name: ') # 호스트 이름 입력
clientSocket.connect((serverName,serverPort))
option = input('Select opthon[1.normal 2.upper 3.lower]: ') # 메세지 옵션 입력
sentence = input('Input lowercase sentence: ') # 메세지 입력

# 호스트 이름, 메세지 옵션, 메세지를 한꺼번에 관리할 수 있도록 딕셔너리 객체로 만들어 준다.
data = {
    "host": username,
    "option": option,
    "message": sentence
}

json_data = json.dumps(data) # 파이썬 객체를 json 문자열로 바꾼다.
clientSocket.send(json_data.encode()) # json 문자열을 바이트 데이터로 바꿔서 보내준다.
modifiedSentence = clientSocket.recv(1024).decode() # 서버로부터 입력을 받는다.
print('From Server : ',modifiedSentence)
clientSocket.close()