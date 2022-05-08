#!/usr/bin/env python
# coding: utf-8

# In[1]:


from emp import Emp


# In[2]:


emps = []


# In[139]:


emps.append(Emp(11, name='smith', phone='010-6541-9870'))
emps.append(Emp(12, name='scott', phone='010-3254-2145'))
emps.append(Emp(13, name='ward', phone='010-2697-1220'))
#emps.index()


# In[3]:


def is_duplicate_num(num):
    nums = []
    for e in emps:
        nums.append(e.num)
    nums.append(num)
    return len(nums)!=len(set(nums))


# In[4]:


def emp_list():
    print("번호\t이름\t전화")
    for emp in emps:
        print(emp)


# In[5]:


def find_emp_name(name): # 검색성공일 경우 해당 사원정보 리턴, 아니면 None 리턴
    emp = None
    for e in emps:
        if e.name==name:
            emp = e
            print(emp)
    return emp




# In[6]:


def update_emp(num, newPhone):
    updated = False
    if is_duplicate_num(int(num)):
        for emp in emps:
            if emp.num==int(num):
                emp.phone = newPhone
                updated = True
    return updated


# In[144]:


def delete_emp(num):
    deleted = False
    for emp in emps:
        if emp.num == num:
            try:
                emps.remove(emp)
                deleted = True
            except ValueError as ve:
                pass
    return deleted


# In[7]:


while True:
    print()
    userinput = input("추가(a), 검색(f), 목록(s), 수정(u), 삭제(d), 종료(x):")
    if userinput == 'a':
        (num, name, phone) = input('번호, 이름, 전화').split()               
        if is_duplicate_num(int(num)) != True:
            emps.append(Emp(int(num),name,phone))
            print('입력 성공') 
        else:
            print('중복된 번호를 입력하셨습니다. 다시 입력해주세요.')
            
    elif userinput == 's':
        emp_list()

    elif userinput == 'f':
        name = input('찾으실 회원이름을 입력해주세요.')
        if find_emp_name(name) == None:
            print('입력된 이름으로 검색 실패')

    elif userinput == 'u':
        num, phone = input('수정할 회원번호, 전화번호를 입력해주세요.').split()
        if update_emp(num, phone):
            print("수정 성공")
        else:
            print("수정 실패")
            
    elif userinput == 'd':
        want = input('삭제할 회원번호를 입력해주세요.')
        if delete_emp(int(want)):
            print("삭제 성공")
        else:
            print("삭제 실패")

    elif userinput == 'x':
        print("프로그램이 종료되었습니다.")
        break
        
    else:
        print("***** 메뉴입력 오류 *****")


# In[188]:


import random
random.randint(1,10)


# In[204]:


from random import randint
randint(1,10)


# ### 파일 다루기

# In[210]:


fstream = open('emp.py', 'r')
data = fstream.read()
print(data)
fstream.close()


# In[211]:


with  open('emp.py', mode='r', encoding='utf-8') as fstream:
    data = fstream.read()
    print(data)


# In[212]:


with  open('emp.py', mode='r', encoding='utf-8') as fstream:
    data = fstream.readlines()  # list
    print(data)

