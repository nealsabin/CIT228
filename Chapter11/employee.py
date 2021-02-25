class Employee:
    def __init__(self,first,last,salary,default_raise=5000):
        self.first=first
        self.last=last
        self.salary=salary
        self.default_raise=default_raise

    def give_raise(self,salary):
        self.salary+=self.default_raise

#couldn't quite figure this out