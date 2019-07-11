class person:
    def __init__(self):
        self.__name=''
    def setname(self, name):
        print('setname() called')
        self.__name=name
    def getname(self):
        print('getname() called')
        return self.__name
    name=property(getname, setname)
p1=person()
p1.setname("vinay")
print(p1.getname())

p1.name="vinay"
print(p1.name)
