import json
from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('172.23.199.194', serverPort)) # 현재 사용자의 컴퓨터의 IP 주소를 입력해준다.
serverSocket.listen(1)
print('The server is ready to receive')

while 1:
    connectionSocket, addr = serverSocket.accept()
    json_data = connectionSocket.recv(1024).decode() # 클라이언트로부터 받은 바이트 데이터를 Json문자열로 바꾼다.
    json_object = json.loads(json_data) # Json문자열을 파이썬 객체로 바꾼다.

    # 옵션에 따라 각기 다른 동작들을 수행한다. 옵션은 data 딕셔너리에서 키 값("option")을 통해 파싱한다.
    if(json_object.get("option") == '1'): # normal
        print("messeage received")
        print("message: ", json_object.get("message"))
        connectionSocket.send(json_object.get("message").encode())

    elif(json_object.get("option") == '2'): # upper
        print('Before:', '[', json_object.get("host"), ']', ':', json_object.get("message"))
        capitalizedSentence = json_object.get("message").upper()
        print('After:', '[', json_object.get("host"), ']', ':', capitalizedSentence)
        connectionSocket.send(capitalizedSentence.encode())

    elif(json_object.get("option") == '3'): # lower
        print('Before:', '[', json_object.get("host"), ']', ':', json_object.get("message"))
        capitalizedSentence = json_object.get("message").lower()
        print('After:', '[', json_object.get("host"), ']', ':', capitalizedSentence)
        connectionSocket.send(capitalizedSentence.encode())

    connectionSocket.close()
