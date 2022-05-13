#!/usr/bin/env python
# coding: utf-8

# # 오늘의 주제
# * MySQL CRUD

# In[1]:


class User:
    
    def __init__(self, num, uid, pwd, email, phone):
        self.num = num
        self.uid = uid
        self.pwd = pwd
        self.email = email
        self.phone = phone
        
    def __str__(self): 
        return f"{self.num}\t{self.uid}\t{self.pwd}\t{self.email}\t{self.phone}"
    
    def __eq__(self, other):
#         print('__eq__')
        return self.num == other.num
    
    


# In[10]:


import pymysql

class UserDAO:
    
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='tjoeun', db = 'mydb', charset = 'utf8')
        print('DB 접속 성공')
    
    def show_list():
#     def show_list(self):
        conn = pymysql.connect(host='localhost', user='root', password='tjoeun', db = 'mydb', charset = 'utf8')
        sql = "SELECT num, uid, phone, email From user"
#         with self.conn.cursor() as curs:
        with conn.cursor() as curs:    
            curs.execute(sql)
#         curs = self.conn.cursor()
#         sql = "SELECT num, uid, phone, email From user"
#         curs.execute(sql)
#         rows = curs.fetchall()
#             userlist = []
            rows = curs.fetchall()
            for (num, name, phone, email) in rows:
                print(num, name, phone, email)
#                 userlist.append(User(num, name, phone, email))
#         self.curs.close()
#         self.conn.close()
        conn.close()
#         return userlist
    def add_user(uid, pwd, phone, email):
#         conn = pymysql.connect(host='localhost', user='root', password='tjoeun', db='mydb', charset='utf8')
# #         # 다수개의 행을 입력하는 경우
#         vals = ("uid", "pwd", "phone", "email") 
# #                 ("Blake","blake", "010-2547-3210", "blake@naver.com"))
#         sql = "INSERT INTO user(uid, pwd, phone, email) VALUES (%s,%s,%s,%s)"

#         with conn.cursor() as cursor:
#             n = cursor.executemany(sql, vals)
#         # cursor.execute(sql,('a','b','c')) 이와같은 문장을 반복해서 다수행을 입력할 수도 있다
#             if n==1:
# #             print('2개행 입력성공')
#                 conn.commit()  # commit을 사용하지 않으면 테이블에 반영되지 않음

#         conn.close()
#         print('사용자 추가 성공')
        
        conn = pymysql.connect(host='localhost', user='root', password='tjoeun', db='mydb', charset='utf8')
        sql = "INSERT INTO user(uid, pwd, phone, email) VALUES (%s,%s,%s,%s)"
        # sql = "SELECT num, uid, phone, email From user LIMIT 10"
        # 다수개의 행을 추가하는 경우 executemany() 를 사용한다
        with conn.cursor() as curs:
            n = curs.execute(sql, (uid, pwd, phone, email) )
            # cursor.execute(sql,('a','b','c')) 이와같은 문장을 반복해서 다수행을 입력할 수도 있다
            if n==1:
#                 print('2개행 입력성공')
                conn.commit()  # commit을 사용하지 않으면 테이블에 반영되지 않음

        conn.close()
        print('사용자 추가 성공')
        
    def delete_user(num):
        conn = pymysql.connect(host='localhost', user='root', password='tjoeun', db='mydb', charset='utf8')
        sql = "DELETE FROM user WHERE num=%s"
        with conn.cursor() as cursor:
            n = cursor.execute(sql, num)
            if n==1:
                print('삭제 성공')
                conn.commit()
        conn.close()
        
    def update_user(num, phone):
        conn = pymysql.connect(host='localhost', user='root', password='tjoeun', db='mydb', charset='utf8')
        sql = "UPDATE user SET phone=%s WHERE num=%s"

        with conn.cursor() as cursor:
            n = cursor.execute(sql, (phone, num) )
            if n==1:
                print('수정 성공')
                conn.commit()
            else:
                print('수정 실패')
        conn.close()
    
    def find_user(num):
        conn = pymysql.connect(host='localhost', user='root', password='tjoeun', db='mydb', charset='utf8')
        sql = "SELECT * FROM user WHERE num = %s"

        with conn.cursor() as curs:
            n = curs.execute(sql, num)
            if n==1:
                rows = curs.fetchall()
                for i in rows:
                    print(i)
        conn.close()
    


# In[11]:


# from user import User
# from dao import UserDAO
# import User
# import UserDAO
import pymysql
while True:
    
    menu = input('목록(s), 추가(a), 검색(f), 수정(u), 삭제(d), 종료(x):').strip()
    
    if menu.upper()=='A':
        uid, pwd, phone, email = input('아이디, 비밀번호, 전화, 이메일:').split()
        UserDAO.add_user(uid, pwd, phone, email)
#         emp = Emp(num,name,phone)
#         if is_duplicate(emp):
#             print('번호 중복, 추가 실패!')
#             continue
#         if add_emp(emp):
#             print('사원정보 추가 성공')
#         else:
#             print('사원정보 추가 실패')
            
    elif menu.upper()=='S':
        UserDAO.show_list()
        
    elif menu.upper()=='F':
        sNum = input('검색할 사원번호:').strip()
        UserDAO.find_user(sNum)
#         if found:
#             print(found)
#         else:
#             print('검색 실패')
            
    elif menu.upper()=='U':
        sNum = input('변경할 사원번호 : ')
        phone = input('전화번호를 입력해주세요 : ')
        UserDAO.update_user(sNum, phone)
           
            
    elif menu.upper()=='D':
        sNum = input('삭제할 사원번호:').strip()
        UserDAO.delete_user(sNum)
         
    elif menu.upper()=='X':
        break;
    else:
        print('메뉴입력 오류')
        
print('프로그램 종료...')


# In[ ]:




