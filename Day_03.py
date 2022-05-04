#!/usr/bin/env python
# coding: utf-8

# # 오늘의 주제
# Collection
# - list, tuple, dictionary, set
# - list : 순서유지, 중복허용
# - tuple : list와 동일특성, 수정/삭제 안됨
# - dictionary : key, value가 쌍으로 저장
# - set : 중복불허, 순서없음
# 함수, 모듈

# In[ ]:


# 프로그램이 시작되면, 추가(a), 검색(f), 목록(s), 수정(u), 삭제(d), 종료(x)

users = []
while True:
    n = input("추가(a) \n"
              "검색(f) \n"
              "목록(s) \n"
              "수정(u) \n"
              "삭제(d) \n"
              "종료(x) \n"
              "원하시는 항목을 선택 해주세요: "
              )
    # while True:
    if n.upper() == 'A':
        num, name, phone = input("사원 번호, 이름, 전화 번호를 입력 해주세요: ").split()
        nums = [user['num'] for user in users] # 기존 등록된 사원번호
        nums.append(num)                      # 새로 추가할 사원번호
        if len(nums) != len(set(nums)):       # 사원번호 중복검사
            print('사원정보 중복, 다시 입력해주세요 \n')
            continue
        else:
            users.append({'num': num, 'name': name, 'phone': phone})
            print("추가 했습니다.\n")

    elif n.upper() == 'F':
        # b = input('검색할 회원번호: ').strip()
        b = input('검색할 회원 이름: ').strip()
        for user in users:
            if b == user['name']:
                s = f"{'num',user['num']}\t{'name',user['name']}\t{'phone',user['phone']}"
                print(s, "\n")
                break
            else:
                print("검색 실패 \n")

    elif n.upper() == 'S':
        # for i in range(len(users)):
        for user in users:
            s = f"{'num',user['num']}\t{'name',user['name']}\t{'phone',user['phone']}"
            print(s)
        print()
        # print(set1)

    elif n.upper() == 'D':
        # c = input('삭제 할 회원번호: ').strip()
        c = input('삭제 할 회원이름: ').strip()
        for i in users:
            if c == i['name']:
                # del users[i]['num']['name']['phone']
                users.remove(i)
                print("삭제 성공 \n")
            else:
                print("삭제 실패 \n")

    elif n.upper() == 'U':
        # b = input('검색할 회원번호: ').strip()
        d = input('수정할 회원 이름: ').strip()
        for j in users:
            if d == j['name']:
                e = input('수정할 번호를 입력해주세요 : ')
                j['phone'] = e
                # users[j]['phone'] = "4"
                print('수정 완료 \n')
            else:
                print("수정 실패 \n")
    elif n.upper() == 'X':
        print("프로그램 종료...")
        break
    else:
        print("메뉴 입력 오류")


# In[ ]:


users = []

def is_duplicate(num):
    nums = [user['num'] for user in users]
    nums.append(num)
    if len(nums) != len(set(nums)):
        return True
    else:
        return False

def is_search(b):
    for user in users:
        if b == user['name']:
            s = f"{'num',user['num']}\t{'name',user['name']}\t{'phone',user['phone']}"
            return s
    return None

def is_list():
    for user in users:
        s = f"{'num',user['num']}\t{'name',user['name']}\t{'phone',user['phone']}"
        print(s)
    print()

def is_del(c):
    for i in users:
        if c == i['name']:
            users.remove(i)
            return True
        else:
            return False

def is_modify(d):
    for j in users:
        if d == j['name']:
            e = input('수정할 번호를 입력해주세요 : ')
            j['phone'] = e
            return True
        else:
            print("수정 실패 \n")

while True:
    n = input("추가(a) \n"
              "검색(f) \n"
              "목록(s) \n"
              "수정(u) \n"
              "삭제(d) \n"
              "종료(x) \n"
              "원하시는 항목을 선택 해주세요: "
              )

    if n.upper() == 'A':
        num, name, phone = input("사원 번호, 이름, 전화 번호를 입력 해주세요: ").split()
        if is_duplicate(num):
            print('사원번호 중복, 다시 입력해주세요')
            continue
        else:
            users.append({'num': num, 'name': name, 'phone': phone})
            print("추가 했습니다.\n")

    elif n.upper() == 'S':
        is_list()

    elif n.upper() == 'F':
        b = input('검색할 회원 이름: ').strip()
        emp = is_search(b)
        if emp:
            print(emp, "\n")
        else:
            print("해당 이름의 사원정보는 없음.")

    elif n.upper() == 'U':
        d = input('수정할 회원 이름: ').strip()
        mod = is_modify(d)
        if mod:
            print('수정 완료 \n')
        else:
            print('수정 실패 \n')

    elif n.upper() == 'D':
        c = input('삭제 할 회원이름: ').strip()
        del_i = is_del(c)
        if del_i:
            print("삭제 성공 \n")
        else:
            print("삭제 실패 \n")

    elif n.upper() == 'X':
        print("프로그램 종료...")
        break
    
    else:
        print()
        print("메뉴 입력 오류")


# In[ ]:


import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# # 클래스 실습
# * 클래스와 인스턴스
# * 초기자 : __init__()
# * 인스턴스 메소드 : 인스턴스에 포함된 메소드

# In[15]:


class Emp:
    
    def __init__(self, num, name, phone):
        self.num = num
        self.name= name
        self.phone = phone
        
    def __str__(self):
        return f"{self.num}\t{self.name}\t{self.phone}"
    
    def __eq__(self, other):
        return self.num == other.num


# In[17]:


e1 = Emp(11, 'Smith', '010-3547-6510')
print(e1)
e2 = Emp(12, 'Blake', '010-3271-1290')
print(e2)
emp_list = [e1, e2]
for e in emp_list:
    print(e)
# Emp.__str__()    


# In[14]:


print(e1.__eq__(e2))
e3 = Emp(12, '', '')
print(e2.__eq__(e3))
print(e2 == e3)
print(e1 == e2)


# In[ ]:


class Emp:

    def __init__(self, num, name, phone):
        self.num = num
        self.name = name
        self.phone = phone

    # def __str__(self):
    #     return f"{self.num}\t{self.name}\t{self.phone}"

    def __str__(self):
        for user in users:
            if name == user['name']:
                s = f"{'num', user['num']}\t{'name', user['name']}\t{'phone', user['phone']}"
                return s

    # def is_search(self):
    #     for user in users:
    #         if name == user['name']:
    #             s = f"{'num', user['num']}\t{'name', user['name']}\t{'phone', user['phone']}"
    #             return s
    #     return None

    def __eq__(self, other):
        return self.num == other.num

    def is_duplicate(self):
        nums = [user['num'] for user in users]
        # nums = [user['num'] for user in Emp]
        nums.append(num)
        if len(nums) != len(set(nums)):
            return True
        else:
            return False

    def is_search(self):
        for user in users:
            if name == user['name']:
                s = f"{'num', user['num']}\t{'name', user['name']}\t{'phone', user['phone']}"
                return s
        return None

    # def is_list(self):
    #     for user in users:
    #         s = f"{'num', user.num['num']}\t{'name', user.name['name']}\t{'phone', user.phone['phone']}"
    #     return s
    #     # return s
    #     # return None

    def is_del(self):
        for i in users:
            if name == i['name']:
                users.remove(i)
                return True
            else:
                return False

    def is_modify(self):
        for j in users:
            if name == j['name']:
                e = input('수정할 번호를 입력해주세요 : ')
                j['phone'] = e
                return True
            else:
                print("수정 실패 \n")


users = []
while True:
    n = input("추가(a) \n"
              "검색(f) \n"
              "목록(s) \n"
              "수정(u) \n"
              "삭제(d) \n"
              "종료(x) \n"
              "원하시는 항목을 선택 해주세요: "
              )

    if n.upper() == 'A':
        num, name, phone = input("사원 번호, 이름, 전화 번호를 입력 해주세요: ").split()
        if Emp.is_duplicate(num):
            print('사원번호 중복, 다시 입력해주세요')
            continue
        else:
            users.append({'num': num, 'name': name, 'phone': phone})
            print("추가 했습니다.\n")

    elif n.upper() == 'S':
        # list1 = Emp.is_list(users)
        list1 = Emp.__str__(users)
        print(list1)
        # Emp.__str__()

    elif n.upper() == 'F':
        b = input('검색할 회원 이름: ').strip()
        emp = Emp.is_search(b)
        if emp:
            print(emp, "\n")
        else:
            print("해당 이름의 사원정보는 없음.")

    elif n.upper() == 'U':
        d = input('수정할 회원 이름: ').strip()
        mod = Emp.is_modify(d)
        if mod:
            print('수정 완료 \n')
        else:
            print('수정 실패 \n')

    elif n.upper() == 'D':
        c = input('삭제 할 회원이름: ').strip()
        del_i = Emp.is_del(c)
        if del_i:
            print("삭제 성공 \n")
        else:
            print("삭제 실패 \n")

    elif n.upper() == 'X':
        print("프로그램 종료...")
        break

    else:
        print()
        print("메뉴 입력 오류")

