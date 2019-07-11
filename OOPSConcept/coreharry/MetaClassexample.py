class MyMeta(type):
    pass

class MyClass(metaclass=MyMeta):
    pass

class MySubclass(MyClass):
    pass



print(type(MyMeta))
print(type(MyClass))
print(type(MySubclass))