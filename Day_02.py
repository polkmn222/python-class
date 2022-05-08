#!/usr/bin/env python
# coding: utf-8

# # 오늘의 주제
# 랜덤, 정렬, 추출, 삭제, 평균값
# 슬라이스
# True, False, and
# 논리 연산자
# 날짜
# list, dictionary, set

# In[24]:


import random as rd
print(rd.randint(0,5))


# In[26]:


# 임의의 정수 10개를 추출하고 내림차순으로 정렬하고, 화면에 표시
import random # 모듈
# rd_num = random.randint(0,10)
list1 = []
for i in range(10):
    rd_num1 = random.randint(0,10)
    list1.append(rd_num1)
    list1.sort(reverse=True)
print(list1)

# 맨 마지막에 있는 정수 1개 삭제
del list1[-1]
print(list1)

# 중간에 위치한 수를 추출하여 화면에 표시
print(list1[int(len(list1)/2)])

# 중간 양쪽에 있는 수의 평균값
a = (list1[int(len(list1)/2)+1] + list1[int(len(list1)/2)-1]) / 2
print(a)


# In[30]:


# 1~10 사이의 정수 중에서 짝수만 선택하여 리스트의 원소에 저장하고
# 홀수는 0으로 변경하여 저장한 후 리스트의 모든 원소를 화면에 표시해 보세요.
list2 = []
for i in range(1, 11):
    if i % 2 !=0:
        i = 0
        list2.append(i)
    else:
        list2.append(i)
print(list2)

nums = [v if v % 2 == 0 else 0 for v in range(1,11)]
print(nums)


# In[34]:


print(nums[4:7])
nums2 = nums[4:7]
nums2[0] = 100
print(nums2[0])


# In[36]:


nums3 = nums # Shallow Copy 얕은 복사
nums3[0] = 100
print(nums3)
print(nums)


# In[37]:


nums4 = nums[:] # Deep Copy 깊은 복사
print(nums4)
nums4[0] = 200
print(nums4)
print(nums)


# In[38]:


nums.append(-5)
print(nums)


# In[40]:


num_list = [4, 5, 6]
print(num_list)
a , b, c = num_list
print(a, b, c)


# In[49]:


# 무작위 정수 10개를 준비하고 처음 3래를 추출하여 튜플에 저장하고
# 튜프의 내용을 화면에 표시
import random as rd
list3 = []

for i in range(10):
    rd_num1 = random.randint(0,10)
    list3.append(rd_num1)

tuple1 = (list3[0], list3[1], list3[2])    
print(tuple1)
print(type(tuple1))

a, b, c = (list3[:3])
tuple11 = (a, b, c)
print(tuple11)
print(type(tuple11))

nums = [v for v in range(1,11)]
tuple2 = (nums[0], nums[1], nums[2]) 
print(tuple2)
print(type(tuple2))


# In[4]:


# 키보드에서 아이디, 암호를 입력 받아서 로그인 하는 기능 구현
# 미리 uid, pwd 리스트를 생성해놓고 몇개의 정보를 준비함
# uid, pwd에는 아이디는 모두 대문자로 준비함
# 로그인에 성공할 때까지 반복해서 시도할 수 있도록 함(3번까지)
# 결국 로그인에 성공하면 '로그인 성공', 아니면 '로그인 실패' 표시

uid_list = ['SMITH', 'JONE', 'ELISE']
pwd_list = ['0000', '1111', '2222']

for i in range(3):
    uid,pwd = input("아이디 패스워드: ").split()
    idx = uid_list.index(uid.upper())
    if (uid_list[idx] == uid.upper()) and (pwd_list[idx] == pwd):
        print('로그인 성공')
        break
    else:
        print('로그인 실패')


# In[1]:


uid_list = ['SMITH', 'JONE', 'ELISE']
pwd_list = ['0000', '1111', '2222']

for i in range(3):
    uid,pwd = input("아이디 패스워드: ").split()
    try:
        idx = uid_list.index(uid.upper())
        if (uid_list[idx] == uid.upper()) and (pwd_list[idx] == pwd):
            print('로그인 성공')
            break
        else:
            print('다시 입력해주세요')
    except ValueError as e:
        print('로그인 실패: ' + str(e))


# In[2]:


1 < 2


# In[3]:


1 < 2 and 3 > 2


# In[6]:


print('a' in ['a', 'b', 'c'])
print('d' in ['a', 'b', 'c'])


# In[13]:


# 파이썬 날짜 다루기
import datetime
# import datetime as dt
from datetime import date

today = datetime.date.today()
print(today)

print(today.year)
print(today.month)
print(today.day)
print(today.weekday())    # 월(0), 화(1)
print(today.isoweekday()) # 월(1), 화(2)


# In[15]:


import datetime
from datetime import date
today = date.today()
print(today)

print(today.year)
print(today.month)
print(today.day)
print(today.weekday())    # 월(0), 화(1)
print(today.isoweekday()) # 월(1), 화(2)


# In[25]:


import datetime
from datetime import date
d = date.today()
t = ['월', '화', '수', '목', '금', '토', '일']
r = d.weekday()
print (str(d.year)+'년', str(d.month)+'월', str(d.day)+'일', t[r]+'요일')


# In[29]:


uid_list = ['SMITH', 'JONE', 'ELISE']
pwd_list = ['0000', '1111', '2222']

for i in range(3):
    uid,pwd = input("아이디 패스워드: ").split()
    if uid.upper() in uid_list:
        idx = uid_list.index(uid.upper())
        if (uid_list[idx] == uid.upper()) and (pwd_list[idx] == pwd):
            print('로그인 성공')
            break
        else:
            print('로그인 실패')


# In[33]:


users = [{}, {}, {}]
print(type(users[0]))
# print(users[0]['key'])


# In[47]:


# 키보드에서 3인의 회원정보를 입력 받는다
# (번호, 이름, 전화)
# 입력을 마치면, 입력된 모든 정보를 리스트로 화면에 표시
users = []
for i in range(3):
    num, name, phone = input("번호, 이름, 전화를 입력하세요: ").split()
    users.append({'num':num, 'name':name, 'phone':phone})

for user in users:
    s = f"{user['num']}\t{user['name']}\t{user['phone']}"
    print(s)


# In[46]:


print(users[2]['phone'])
users[2]['phone'] = "4"
print(users[2]['phone'])


# In[52]:


users[2]['phone'] = "전화기 분실"
for user in users:
    s = f"{user['num']}\t{user['name']}\t{user['phone']}"
    print(s)


# In[53]:


del users[2]['phone']
for user in users:
    s = f"{user['num']}\t{user['name']}\t{user.get('phone', '전화기분실')}"
    print(s)


# In[58]:


users = []
for i in range(3):
    num, name, phone = input("번호, 이름, 전화를 입력하세요: ").split()
    users.append({'num':num, 'name':name, 'phone':phone})

num = input('검색할 회원번호: ').strip()    
for user in users:
    if num==user['num']:
        s = f"{user['num']}\t{user['name']}\t{user['phone']}"
        print(s)
        break


    


# In[ ]:


# list , set , dictionary
# list : 순서 유지, 중복 활용
# set  : 순서 없음, 중복 불허
# dict : key, value 쌍으로 저장 


# In[59]:


print(set([1, 1, 1, 1, 2]))


# In[60]:


set1 = set([1, 1, 1, 1, 2])
print(len(set1))


# In[64]:


# 1 ~ 10 사이의 정수 중에서 임의로 한 개를 추출하여 중복되지 않도록 7개를 추출하려고 한다.
# 추출된 원소를 정렬하여 화면에 표시한다
import random # 모듈

set2 = set([])
#print(type(set2))
while True:
    rd_num1 = random.randint(1,11)
    set2.add(rd_num1)
    if len(set2) > 6 :
        print(set2)
        break


# In[65]:


import random 

set2 = set([])

while True:
    rd_num1 = random.randint(1,11)
    set2.add(rd_num1)
    if len(set2) == 7 :
        print(set2)
        break

