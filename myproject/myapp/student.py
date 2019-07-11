from django.http import HttpResponse,request
class studentinfo:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
obj=studentinfo("vinay",21,56)
