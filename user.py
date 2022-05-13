class User:
    def __init__(self,num,name=None,phone=None,email=None):
        self.num = num
        self.name = name
        self.phone = phone
        self.email = email
    
    def __str__(self):
        return "{}\t{}\t{}\t{}".format(self.num,self.name,self.phone,self.email)
    
    def __eq__(self, other):
        return self.num==other.num