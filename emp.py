class Emp:
    def __init__(self, num, name=None, phone=None):
        self.num = num
        self.name = name
        self.phone = phone
        
    def __str__(self): 
        return f"{self.num}\t{self.name}\t{self.phone}"
    
    
