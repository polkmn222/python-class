#!/usr/bin/env python
# coding: utf-8

# # 오늘의 주제
# * 파일 열기 : open()
# * CRUD      : read, write, readline
# * 파일닫기  : close()

# In[17]:


fobj = open('emp.py', 'r')
# open('emp.py')
type(fobj) # _io.TextIOWrapper
dir(fobj)  # Iterator, __next__(), 반복문에 적용 가능
fobj.close()


# In[18]:


fobj = open('emp.py', 'r')
for data in fobj:
    # print(data, end='') # 프린트의 디폴트(\n) 개행을 하지마라 # Keyword Arguments
    print(data.rstrip()) # 오른쪽 끝에 있는 공백제거
fobj.close()


# In[19]:


from collections.abc import Iterable, Iterator
nums = [1,2,3]
dir(nums)
isinstance(nums, Iterable) # True, isinstance (Java : intance of 메소드와 동일), __getitem__()이 존재한다
# nums.__iter__() # for of 안에서 사용가능
isinstance(nums, Iterator) # False


# In[20]:


# itr = nums.__getitem__(0)
# print(nums[0])
itr = nums.__iter__() # next만 호출, 인스턴스 안에 있는 메소드

isinstance(itr, Iterator) # True


# In[21]:


# nums.__iter__()
iter(nums) # 함수(클래스 밖)


# In[22]:


isinstance(fobj, Iterator)
isinstance(fobj, Iterable)
dir(fobj)


# In[23]:


fobj = open('emp.py', 'r')
fdata = fobj.read()
print(fdata)
print(type(fdata)) # str
fobj.close()


# In[24]:


fobj = open('emp.py', 'r')
datalist = fobj.readlines()
print(type(datalist)) # list


for line in datalist:
#     print(line, end="")
    print(line.rstrip())
fobj.close()    


# In[25]:


fobj = open('emp.py', 'r')
print(fobj.__next__().rstrip())
print(fobj.__next__().rstrip())
print(fobj.__next__().rstrip())
print(fobj.__next__().rstrip())
print(fobj.__next__().rstrip())

fobj.close()


# In[26]:


fobj = open('emp.py', 'r')
# fobj.__next__()
print(next(fobj).rstrip())
print(next(fobj).rstrip())
print(next(fobj).rstrip())
print(next(fobj).rstrip())
print(next(fobj).rstrip())
fobj.close()


# In[27]:


with open('emp.py', 'r') as fobj:
    for line in fobj:
        print(line.rstrip())
        
fobj.close()        


# In[28]:


# Emp 클래스가 포함된 모듈을 임포트한다
from emp import Emp

# with 절을 이용하여 emps.txt를 읽기모드로 열고 객체를 fobj에 저장
with open('emps.txt', 'r') as fobj:
    # 한 행을 읽어서 공백 기준으로 쪼갠다
    for line in fobj:
        (num,name,phone) = line.strip().split()
        print(Emp(num,name,phone)) 


# In[29]:


from emp import Emp

with open('emps.txt', 'r') as fobj:
    for line in fobj:
        tup = line.strip().split()
        emp = Emp(tup[0], tup[1], tup[2])
        print(emp)


# In[30]:


list = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

# 리스트 안에서 for 문 사용하기 1
list = [ num * 3 for num in list ]
print(list)


# In[34]:


from emp import Emp

emps = []
with open('emps.txt', 'r') as fobj:
    for line in fobj:
        num,name,phone = line.strip().split()
        emps.append(Emp(num,name,phone))

# 목록을 받아서 화면에 표시한다
show_list(emps)


# In[35]:


# 목록을 받아서 화면에 표시한다
# Emp 클래스가 포함된 모듈을 임포트한다

def show_list(emps):
    for emp in emps:
        print(emp)

from emp import Emp

emps = []
with open('emps.txt', 'r') as fobj:
    for line in fobj:
        num,name,phone = line.strip().split()
        emps.append(Emp(num,name,phone))

# 목록을 받아서 화면에 표시한다
show_list(emps)


# In[36]:


# 파일에 한 행 추가
# open, append mode, write
fobj = open('filename', 'a')
fobj.write('line\n')
fobj.close()


# In[37]:


from emp import Emp

def load_emps():
    emps = []
    with open('emps.txt', 'r') as fobj:
        for line in fobj:
            num,name,phone = line.strip().split()
            emps.append(Emp(num,name,phone))
    return emps


# In[38]:


def save_emp(emp):
    line = "{} {} {}".format(emp.num, emp.name, emp.phone)
    with open('emps.txt', 'a') as fobj:
        fobj.write(line + '\n')


# In[39]:


show_list(load_emps())


# In[40]:


# 키보드에서 num,name,phone을 입력받아서 emps.txt에 한 행으로 추가
# 목록보기 기능을 실행하면 추가된 정보가 표시되어야 함

num, name, phone = input('번호 이름 전화: ').strip().split() # 키보드에서 한 사원정보를 입력 받는다
save_emp(Emp(num,name,phone)) # 사원정보를 파일에저장
show_list(load_emps()) # 저장된 데이터 확인, 목록을 화면에 표시한다


# In[ ]:


# 키보드에서 입력된 사원번호를 키워드로 emps.txt에서 검색하여
# 검색된 사원정보를 화면에 표시
# find_emp(emp) : Emp 객체 리턴
# [Emp, Emp...]

nums = [3, 4 ,5]
5 in nums
10 in nums    # 10==3, 10==4, 10==5
emp in emps   # emp==emps[0], emp==emps[1], ...


# In[44]:


# 파일 데이터를 로드
emplist = load_emps()
# 위에서 로드된 리스트로부터 키보드에서 입력된 사원번호의 Emp객체의 포함여부 확인
sNum = input('검색하려는 사원의 번호: ')
emp = Emp(sNum)

found = None
if e in emplist:
    if e.name == sNum:
        print('찾음')
    found = emplist[emplist.index(emp)]
    
if found:
   print(found)
else:
   print('검색실패')


# In[45]:


def find_emp(emp):
    found = None
    
    if emp in load_emps():
        found = emplist[emplist.index(emp)]
    return found


# In[47]:


sNum = input('검색하려는 사원의 번호: ')
emp = Emp(sNum.strip())
found = find_emp(emp)
if found:
    print(found)
else:
    print('검색실패')


# In[ ]:


Emp('11') in load_emps()


# In[50]:


# 키보드에서 사번, 전화번호를 받아서 해당 사원의 정보를 갱신한다
# update_emp(emp) : True/False
num, phone = input('사원번호 전화: ').strip().split()
key = Emp(num, phone=phone)
print(key)


# In[51]:


def overwrite(emplist):
    try:
        with open('emps.txt', 'w') as fobj:
            for emp in emplist:
                line = "{} {} {} ".format(emp.num, emp.name, emp.phone)
                fobj.write(line + "\n")
        return True
    except:
        return False


# In[52]:


def update_emp(key):
    updated = False
    emplist = load_emps()
    if key in emplist:
        emplist[emplist.index(key)].phone = key.phone
        updated = overwrite(emplist)
    return updated    


# In[54]:


if update_emp(key):
    print('수정성공')
else:
    print('수정실패')
show_list(load_emps())    


# In[ ]:


def delete_emp(key):
    deleted = False
    emplist = load_emps()
    if key in emplist:
        emplist.remove(key)
        deleted = overwrite(emplist)
    return deleted


# In[ ]:


# 로드, 리스트에서 삭제대상 찾아서 삭제, 수정된 리스트로 파일 덮어쓰기
sNum = input('삭제할 사원번호:')
key = Emp(sNum.strip())


# In[ ]:


deleted = delete_emp(key)
if deleted:
    print('삭제 성공')
else:
    print('삭제 실패')


# # 객체 직렬화(Serialization)
# 메모리상에 저장된 객체를 파일이나 네트워크로 전송할 때 필요함

# In[ ]:


emp = Emp(15, 'Scott', '000-1111-2222')
with open('empObj.pickle', 'wb') as fw:
    pickle.dump(emp, fw)

