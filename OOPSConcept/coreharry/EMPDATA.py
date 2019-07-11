class Employee:

    department ="HR"
    sal_inc=2
    def __init__(self,name, age,mobile_number):
        self.name=name
        self.age=age
        self.mobile_number=mobile_number
    def reviseslareay(self,salary):
        self.salary=salary*self.sal_inc
        return self.salary



obj=Employee("vinay",21,8554031093)
#print(obj.__dict__)
#print(Employee.__dict__)
print(Employee.department)
final_sal=obj.reviseslareay(20)
print(final_sal)
print(obj.age)