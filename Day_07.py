#!/usr/bin/env python
# coding: utf-8

# # 오늘의 주제
# * Thread
# * Socket
# - 전구 소켓
# - 소켓
# - 접속구
# 인터넷에 연결된 다른 컴퓨터에 접속하기 위한 접속구 역할
# tcp/ip protocol을 사용하여 다른 시스템과 통신하려고 할 때
# tcp/ip socket

# In[ ]:


# 키보드에서 숫자가 입력될 때 마다 해당 숫자로부터 1씩 감소하면서 출력하는
# 기능 숫자가 0에 도달할 때 까지 반복해서 1초에 한 번씩 화면에 표시함
# 5 4 3 2 1 0


# In[ ]:


import threading
import time
import datetime

class CountDownThread(threading.Thread):
    
    def __init__(self, name, num):
        threading.Thread.__init__(self)   
        self.name = name
        self.num = num
        print(name, 'instanciated')
        self.daemon = True
        
        
    def run(self):
        print(self.name, ' 쓰레드 시작')
        while True:
            self.num -= 1
            print(self.num)
            if self.num == 0:
                print(self.name + ' 쓰레드 종료')
                break
            time.sleep(1)    


# In[ ]:


num = input('카운트 다운 수 입력: ')
CountDownThread(num, int(num)).start()


# In[ ]:


# 서버에 접속, 데이터 송수신
# 서버는 클라이언트 접속 대기 상태로 존재해야 함
# 서버는 특정 클라이언트 간의 통신 중개 역할

from socket import *
import pickle
import time

clientSock = socket(AF_INET, SOCK_STREAM) # 소켓 생성
clientSock.connect(('127.0.0.1', 1122))   # 서버에 접속

msg = clientSock.recv(1024)               # 서버 데이터 수신 대기
print(msg.decode('utf-8'))                # 서버로부터 수신된 데이터를 화면에 표시

clientSock.send('클라이언트 메시지'.encode('utf-8'))

time.sleep(1)
print('클라이언트 종료...')


# In[ ]:


from socket import *
import pickle
import time


# In[ ]:


from socket import *
import pickle
import time


serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', 1122))
serverSock.listen(1)

print('서버 대기 중...')
com_soc, addr = serverSock.accept() # 클라이언트 접속시까지 대기함

print(str(addr), '에서 접속됨')

msg = '서버에 접속됨'
com_soc.send(msg.encode('utf-8'))

msg = com_soc.recv(1024)
print(msg.decode('utf-8'))

time.sleep(1)
print('서버 종료...')


# In[ ]:


class ChatMsg:
    def __init__(self, contents, to=None, frm=None, attach=None):
        self.contents = contents
        self.to = to
        self.frm = frm
        self.attach = attach
        
    def __str__(self):
        return "contents={}, frm={}, to={}".format(self.contents, self.to, self.frm)


# In[ ]:


from socket import *
import time
import pickle
from chat import ChatMsg

#%%
serverSock=socket(AF_INET, SOCK_STREAM)
serverSock.bind(('',1122))
serverSock.listen(1)

print('서버 대기중')
com_soc, addr = serverSock.accept()

print(str(addr), '에서 접속됨')

msg = ChatMsg('서버에 접속됨')
com_soc.send(pickle.dumps(msg))

msg = com_soc.recv(1024)
chatmsg = pickle.loads(msg)
print(chatmsg)


time.sleep(1)
print('서버종료')


# In[ ]:


from socket import *
import threading
import time
import pickle
from chat import ChatMsg

class ChatThread(threading.Thread):
    
    def __init__(self, soc, addr, soc_list, num):
        threading.Thread.__init__(self)
        print('ChatThread 시작됨')
        self.soc = soc
        self.addr = addr
        self.soc_list = soc_list
        self.num = num
        
    def run(self):
        for i,s in self.soc_dict.items():
            print(i,s)
            if s is self.soc:
                continue
            cmsg = pickle.dumps(ChatMsg(str(self.addr) + '접속'))
            s.send(cmsg)
#         msg = ChatMsg('서버 접속 성공')
#         self.soc.send(pickle.dumps(msg))
#         rem_idx = -1
        while True:
            try:
#                 msg = self.soc.recv(1024)
                msg = self.soc.recv(7168)
                chatmsg = pickle.loads(msg)
                if chatmsg.to:
                    soc_dict[chatmsg.to].send(msg)
                else:
                    for i,s in self.soc_dict.items():
                        if s is self.soc:
#                             rem_idx = i
                            continue
#                 for s in self.soc_list:
#                     if s == self.soc:
#                         continue
                    s.send(msg)
            except:
                print(str(self.addr)+' 퇴장')
#                 for s in self.soc_list:
#                     if s is self.soc:
#                         continue
#                 del self.soc_dict[rem_idx]
                del self.soc_dict[self.num]
                for i,s in self.soc_dict.items():
                    cmsg = pickle.dumps(ChatMsg(str(self.addr) + '퇴장'))
                    s.send(cmsg) 
                break
        print('ChatThread 종료')  
            


# In[ ]:


serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', 1122))
serverSock.listen(1)

soc_list = []
soc_dict = {}
num = 0

while True:
    print('서버 대기 중...')
    soc, addr = serverSock.accept()   # 클라이언트 접속시까지 대기함
#     soc_list.append(soc)
    num += 1
    soc_dict[num] = soc
#     soc_list[num] = soc
#     ChatThread(soc, addr, soc_list, num).start()
    ChatThread(soc, addr, soc_dict, num).start()

print('서버 종료...')

