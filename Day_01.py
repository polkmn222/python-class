#!/usr/bin/env python
# coding: utf-8

# # 오늘의 주제
# * 파이썬 인터프리터의 이해
# * Jupyter notebook 활용하기
# * 주석문의 종류

# In[8]:


print('Hello World')
# CTRL + ENTER, ALT + ENTER


# In[11]:


a = 5
b = 7
c = a + b # CTRL + ENTER, SHIFT + ENTER
print('c = ', c)


# In[15]:


msg = "Hello"
print(msg)
msg = 'World'
print(msg)
msg = """This
            is
            String
                test"""
# print(msg)
"""
print("a")
print("b")
print("c")
"""


# In[16]:


# a = ""Hello'
# a


# In[17]:


msg = "Hello 'World'"
print(msg)


# In[19]:


name = "ada lovelace"
title = name.title()
print(name.title())
print(title)


# In[20]:


name = "Ada lovelace"
print(name.upper())
print(name.lower())


# In[22]:


print(dir(name))
print(help(str))


# In[23]:


name = "Smith"
age = 29
info = f"{name} {age}"
print(info)


# In[24]:


name = input('이름을 입력해주세요:')


# In[25]:


# 키보드에서 번호, 이름, 전화번호를 입력받아서 서식 문자열로 화면에 표시해보세요.
number = input('번호를 입력해 주세요: ')
name = input('이름를 입력해 주세요: ')
phone = input('전화번호를 입력해 주세요: ')
print(number, name, phone)


# In[2]:


greeting = "Hello "
newGreetring = greeting.rstrip() # Shift Tab
print(greeting)
print(newGreetring)


# In[3]:


a, b, c = 1, 2, 3
print(a, b, c)


# In[5]:


nums = [1, 2, 3]
print(nums)
a, b, c = nums
print(a)


# In[9]:


msg = 
"""
ABC
"""
print(msg)
msg = 
'''
A B C
'''
print(msg)


# In[5]:


names = ['smith', 'scott', 'jone'] # List
print(len(names))
print(names[1])
print(names[1].title())


# In[7]:


print(names[0], names[2])


# In[8]:


names[0], names[2] # () 생략 Tuple


# In[15]:


print(type(['a']))
# 원소가 한개인 Tuple 선언하고 자료형 확인하기
data = (a, b, c)
data = (10)
data = (10,)
print(type(('a',)))


# In[24]:


num = [1, 2, 3]
num[2] = 5
print(num)
dir(num)
num.append(4) # 값 맨 뒤에 추가
print(num)
num.remove(5) # 값 삭제
print(num)
del num[1] # 방 번호 삭제
print(num)


# In[17]:


data = (1, 2, 3)
data = 1, 2, 3 # () 생략
print(type((data)))


# In[26]:


print(data)
print(data[-1]) # 끝 방


# In[27]:


for x in [3, 5, 7]:
    print(x)


# In[28]:


for i in range(0, 3):
    print(i)


# In[ ]:


# 키보드에서 회원의 정보(번호, 이름, 전화) 를 입력받아서 리스트에 저장하는 프로그램을 작성
# 3인의 회원정보를 입력 받아서 리스트에 저장하고 화면에 표시해보세요.
num = []
name = []
phone = []
for i in range(3):
    strMem = input('번호 이름 전화:')
    meminfo = strMem.split(' ')
    
    num.append(meminfo[0])
    name.append(meminfo[1])
    phone.append(meminfo[2])
for i in range(3):
    print(num[i], name[i], phone[i])    


# In[ ]:


newInfo = input('수정할 회원번호 전화: ')

n, newPhone = newInfo.split(' ')
idx = num.index(n) # 값을 사용하여 인덱스를 구함
phone[idx] = newPhone # 전화번호 업데이트

print('\n','수정된 정보')
for i in range(0,3):
    print (num[i], name[i], phone[i])


# In[ ]:


for i in range(0,3):
    print(num[i], name[i], phone[i])

del_num = input('삭제할 회원번호:')
try:
    idx = num.index(del_num)
    del num[idx]
    print('삭제 성공')
except ValueError as e:
    print('삭제 실패' + str(e))


# In[1]:


motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop() 
print(motorcycles)
print(popped_motorcycle)


# In[3]:


cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)


# In[4]:


cars.sort(reverse=True)
print(cars)


# In[9]:


print(sorted(cars))
copy_list = sorted(cars)
print('사본:',copy_list)
print('원본:',cars)


# In[14]:


print(cars)
cars.reverse() # IN PLACE 원본을 바꾼다
print(cars)


# In[15]:


nums = [2, 1, 3]
nums.reverse()
print(nums)


# In[17]:


import random

rd_num = random.randint(0,10)
print(rd_num)


# In[25]:


import random
# 임의의 정수 한개를 구함(5~10)
# 위에서 구해진 갯수만큼의 임의의 정수를 구함
# 표시 예)
# 1. 6
# 2. 2
rd_num = random.randint(5,10)
list1 = []
for i in range(0, rd_num):
    rd_num1 = random.randint(0,10)
    list1.append(rd_num1)
    print(i+1, list1[i])    

