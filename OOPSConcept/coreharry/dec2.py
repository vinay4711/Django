class employe:
    def __init__(self,first,last):
        self.first=first
        self.last = last
    @property
    def email(self):
        return "{}.{}@gmail.com".format(self.last,self.first)
    @email.setter
    def email(self,name):
        #change email id format
        f1,f2=name.split(" ")
        self.last=f1
        self.first=f2


    @property
    def fullname(self):
        return '{}{}'.format(self.first,self.last)
    @fullname.setter
    def fullname(self,name):
        first,last=name.split(" ")
        self.first=first
        self.last = last
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = employe('John', 'Smith')
emp_1.fullname = "Corey Schafer"
emp_1.email= "vinay kumar123"
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname