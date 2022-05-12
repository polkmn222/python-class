#!/usr/bin/env python
# coding: utf-8

# # 오늘의 주제
# * 채팅
# * 파일 전송
# * mysql

# In[ ]:


from socket import *
import pickle
import time
import threading
from chat import ChatMsg

class SendThread(threading.Thread):
    
    def __init__(self, soc):
        threading.Thread.__init__(self)
        self.soc = soc 
    
    def run(self):
        while True:
            sMsg = input('입력: ')          # 3/hello
            in_list = sMsg.split('/')       # ['3', 'hello']
            chatmsg = None
            if len(in_list) == 1:           # 모두에게 보내는 메시지
                chatmsg = ChatMsg(sMsg)
            elif len(in_list) == 2:
                n, msg = in_list
                chatmsg = ChatMsg(msg, to=int(n))
#             chatmsg = pickle.dumps(ChatMsg(sMsg))
#             self.soc.send(chatmsg)
            self.soc.send(pickle.dumps(chatmsg))

    
clientSock = socket(AF_INET, SOCK_STREAM)  # 소켓 생성
clientSock.connect(('127.0.0.1', 1122))    # 서버에 접속

SendThread(clientSock).start()

while True:
    msg = clientSock.recv(1024)                
    print(pickle.loads(msg))

print('클라이언트 종료...')


# In[ ]:


from socket import *
import pickle
import time
from chat import ChatMsg
import threading


class sendThread(threading.Thread):
    def __init__(self, soc):
        threading.Thread.__init__(self)
        self.soc = soc
        
    def run(self):
        while True:
                sMsg = input('입력 : ')
                in_list = sMsg.split('/')
                chatmsg = None
                if len(in_list)==1:                            # 모두에게 보내는 메시지
                    chatmsg = ChatMsg(sMsg)
                elif len(in_list)==2:                          # 특정인에게 보내는 메시지
                    n, msg = in_list
                    chatmsg = ChatMsg(msg, To = int(n))
                elif len(in_list)==3:                          # 특정인에게 파일첨부 보내기
                    n, msg, fname = in_list
                    with open(fname, 'rb') as fin:
                        fdata = fin.read()
                        chatmsg = ChatMsg(msg, To = int(n), attach = fdata)
                        print('보내는 파일크기 : ', len(chatmsg.attach))
                cmsg = pickle.dumps(chatmsg)
                self.soc.send(cmsg)




soc = socket(AF_INET, SOCK_STREAM)   # 소켓 생성
soc.connect(('127.0.0.1', 1122))     # 서버에 접속 ip주소/포트번호

sendThread(soc).start()

while True:
    msg = soc.recv(7168)        # 서버 데이터 수신 대기 (한꺼번에 받을 데이터 크기1KB )
    smsg = pickle.loads(msg)
    print(smsg)                 # 서버로부터 수신된 데이터를 화면에 표시
    if smsg.attach:
        print('받은 파일크기 : ', len(smsg.attach))
        with open('copy.jpg', 'wb') as fout:
            fout.write(smsg.attach)
            print('파일 저장 성공')

print('클라이언트 종료..~')


# In[ ]:


n, msg, fname = '3/msg/fname'.split('/')
with open('test.jpg', 'rb') as fin:
    img_data = fin.read()
#     print(type(img_data))
    ChatMsg(msg, to=int(n), attach=img_data)
    
print('이미지 로드 완료')    


# In[ ]:


# mysql
import pymysql


# In[ ]:


import pymysql
# 152.70.92.222
# MySQL Connection 연결
# conn = pymysql.connect(host='localhost', user='root', password ='tjoeun', db = 'world', charset='utf-8')
conn = pymysql.connect(host='localhost', user='root', password='tjoeun', db = 'mydb', charset = 'utf8')

curs = conn.cursor()

sql = "SELECT num, uid, phone, email From user LIMIT 10"
curs.execute(sql)

rows = curs.fetchall()
for (num, name, phone, email) in rows:
    print(num, name, phone, email)
    
curs.close()
conn.close()


# In[ ]:


import pymysql

# MySQL Connection 연결

conn=pymysql.connect(host='localhost', user='root',password='tjoeun', db='world', charset='utf8')


#Connection 으로부터 Cursor 생성
# Dictoionary Cursor 생성
curs = conn.cursor(pymysql.cursors.DictCursor)

# SQL 실행
sql = "SELECT code, name, continent FROM country WHERE code=%s AND continent=%s"
curs.execute(sql, ('KOR','ASIA'))

# 데이타 Fetch
rows = curs.fetchall()
for row in rows:
    print(row)
    print(row['code'], row['name'], row['continent'])
curs.close()
#Connection 닫기
conn.close()


# In[ ]:


import pymysql
 
# MySQL Connection 생성
conn = pymysql.connect(host='localhost', user='root', password='tjoeun',
                       db='mydb', charset='utf8')
 
# 다수개의 행을 입력하는 경우
vals = (("Smith","smith", "010-5417-3251", "smith@daum.net"), 
        ("Blake","blake", "010-2547-3210", "blake@naver.com"))
sql = "INSERT INTO user(uid, pwd, phone, email) VALUES (%s,%s,%s,%s)"
# sql = "SELECT num, uid, phone, email From user LIMIT 10"
# 다수개의 행을 추가하는 경우 executemany() 를 사용한다
with conn.cursor() as cursor:
    n = cursor.executemany(sql, vals )
    # cursor.execute(sql,('a','b','c')) 이와같은 문장을 반복해서 다수행을 입력할 수도 있다
    if n==2:
        print('2개행 입력성공')
        conn.commit()  # commit을 사용하지 않으면 테이블에 반영되지 않음

conn.close()
print('사용자 추가 성공')


# In[ ]:


import pymysql
 
# MySQL Connection 생성
conn = pymysql.connect(host='localhost', user='root', password='tjoeun',
                       db='mydb', charset='utf8')
 
# Update
sql = "UPDATE user SET phone=%s WHERE num=%s"

with conn.cursor() as cursor:
    n = cursor.execute(sql, ('010-3333-7777', 6) )

    if n==1:
        print('수정 성공')
        conn.commit()

conn.close()


# In[ ]:


import pymysql
 
# MySQL Connection 생성
conn = pymysql.connect(host='localhost', user='root', password='tjoeun',
                       db='mydb', charset='utf8')
 
# Update
sql = "DELETE FROM user WHERE num=%s"

with conn.cursor() as cursor:
    n = cursor.execute(sql, 1)

    if n==1:
        print('삭제 성공')
        conn.commit()

conn.close()

