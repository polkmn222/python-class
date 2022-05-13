import pymysql
from user import User

class UserDAO:
    
    def __init__(self):
        self.conn = pymysql.connect(host='152.70.92.222', user='myuser', password='myuserpwd',
                      db='mydb', charset='utf8')
        print('DB 연결 성공')
        
    def add(self, user):
        sql = 'INSERT INTO user VALUES (%s,%s,%s,%s)'
        
        with self.conn.cursor() as curs:
            n = curs.execute(sql, (user.num, user.name, user.phone, user.email))
            inserted = False
            if n==1:
                self.conn.commit()
                inserted = True
            else:
                inserted = False
        self.conn.close()
        return inserted
        
    def list_all(self):
        sql = 'SELECT * FROM user'
        userlist = []
        with self.conn.cursor() as curs:
            curs.execute(sql)
            rows = curs.fetchall()
            for (num,name,phone,email) in rows:
                userlist.append(User(num,name,phone,email))
        self.conn.close()
        return userlist
    
    def find_by_num(self, num):
        sql = 'SELECT * FROM user WHERE num=%s'
        user = None
        with self.conn.cursor() as curs:
            curs.execute(sql, num)
            rows = curs.fetchall()
            num,name,phone,email = rows[0]
            user = User(num,name,phone,email)
        self.conn.close()
        return user
    
    def find_by_name(self, name):
        sql = 'SELECT * FROM user WHERE name=%s'
        user = None
        with self.conn.cursor() as curs:
            curs.execute(sql, name)
            rows = curs.fetchall()
            num,name,phone,email = rows[0]
            user = User(num,name,phone,email)
        self.conn.close()
        return user
    
    def update_user(self, user):
        sql = 'UPDATE user SET phone=%s, email=%s WHERE num=%s'
        updated = False
        with self.conn.cursor() as curs:
            n = curs.execute(sql, (user.phone, user.email, user.num))
            if n==1:
                self.conn.commit()
                updated = True
            else:
                updated = False
        self.conn.close()
        return updated
    
    def delete_user(self, num):
        sql = 'DELETE FROM user WHERE num=%s'
        deleted = False
        with self.conn.cursor() as curs:
            n = curs.execute(sql, num)
            if n==1:
                self.conn.commit()
                deleted = True
            else:
                deleted = False
        self.conn.close()
        return deleted 