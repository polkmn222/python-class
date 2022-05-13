#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pymysql
 
# MySQL Connection 연결
#conn = pymysql.connect(host='localhost', user='root', password='tjoeun',
#                       db='world', charset='utf8')

conn = pymysql.connect(host='152.70.92.222', user='myuser', password='myuserpwd',
                      db='mydb', charset='utf8')
 
# Connection 으로부터 Cursor 생성
curs = conn.cursor()
 
# SQL문 실행
sql = "SELECT num, name, phone, email FROM user LIMIT 10"
curs.execute(sql)
 
# 데이타 Fetch
rows = curs.fetchall()  # ((),(),...)

for (num,name,phone,email) in rows:
    print(num,name,phone,email)

curs.close()    
# Connection 닫기
conn.close()


# In[ ]:


class User:
    def __init__(self, num, name=None, phone=None, email=None):
        self.num = num
        self.name = name
        self.phone = phone
        self.email = email
        
    def __str__(self):
        return '{}\t{}\t{}\t{}'.format(self.num, self.name, self.phone, self.email)
    
    def __eq__(self, other):
        return self.num == other.num


# In[ ]:


import pymysql

class TestDAO:
    def __init__(self ):
        self.conn = pymysql.connect(host='152.70.92.222', user='myuser', password='myuserpwd',
                      db='mydb', charset='utf8')
        print('DB 접속 성공')
        
    def list_all(self):
        sql = 'SELECT * FROM user'
        with self.conn.cursor() as curs:
            curs.execute(sql)
            rows = curs.fetchall()
            userlist = []
            for num,name,phone,email in rows:
                userlist.append(User(num,name,phone,email))
        self.conn.close()
        return userlist


# In[ ]:


dao = TestDAO()
ulist = dao.list_all()
for u in ulist:
    print(u)


# In[ ]:


import pymysql
 
# MySQL Connection 생성
conn = pymysql.connect(host='localhost', user='root', password='tjoeun',
                       db='test', charset='utf8')
 
# 다수개의 행을 입력하는 경우
vals = (("Smith", "010-5417-3251", "smith@daum.net"), 
        ("Blake", "010-2547-3210", "blake@naver.com"))
sql = "INSERT INTO user(name, phone, email) VALUES (%s,%s,%s)"
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
                       db='test', charset='utf8')
 
# Update
sql = "UPDATE user SET phone=%s WHERE num=%s"

with conn.cursor() as cursor:
    n = cursor.execute(sql, ('010-3333-7777', 14) )

    if n==1:
        print('수정 성공')
        conn.commit()

conn.close()


# In[ ]:


import pymysql
 
# MySQL Connection 생성
conn = pymysql.connect(host='localhost', user='root', password='tjoeun',
                       db='test', charset='utf8')
 
# Update
sql = "DELETE FROM user WHERE num=%s"

with conn.cursor() as cursor:
    n = cursor.execute(sql, 15 )

    if n==1:
        print('삭제 성공')
        conn.commit()

conn.close()


# In[1]:


def list_all():
    udao = UserDAO()
    userlist = udao.list_all()
    for u in userlist:
        print(u)


# In[2]:


def add(user):
    udao = UserDAO()
    return udao.add(user)


# In[3]:


def find_user():
    n_m = input('번호(n)로 검색 혹은 이름(m)으로 검색:').strip().upper()
    udao = UserDAO()
    user = None
    if n_m=='N':
        sNum = input('검색대상 번호:').strip()
        user = udao.find_by_num(int(sNum))
    elif n_m=='M':
        name = input('검색대상 이름:').strip()
        user = udao.find_by_name(name)
    print(user)


# In[4]:


def update_user():
    num,phone,email = input('번호 전화 메일:').strip().split()
    udao = UserDAO()
    return udao.update_user(User(int(num), phone=phone, email=email))


# In[5]:


def delete_user():
    num = input('삭제할 대상 번호:').strip()
    udao = UserDAO()
    return udao.delete_user(int(num))


# In[6]:


from user import User
from dao import UserDAO

menu = "목록(s), 추가(a), 검색(f), 수정(u), 삭제(d), 종료(x):"
user_input = None

while True:
    user_input = input(menu).upper()
    
    if user_input=='A':
        num,name,phone,email = input('번호 이름 전화 이메일 입력:').strip().split()
        user = User(int(num),name,phone,email)
        if add(user):
            print('추가 성공')
        else:
            print('추가 실패')
    elif user_input=='S':
        list_all()
    elif user_input=='F':
        find_user()
    elif user_input=='U':
        if update_user():
            print('수정 성공')
        else:
            print('수정 실패')
    elif user_input=='D':
        if delete_user():
            print('삭제 성공')
        else:
            print('삭제 실패')
    elif user_input=='X':
        break
    else:
        print('-------- 메뉴입력 오류---------')
        
print('프로그램 종료...')


# In[ ]:




