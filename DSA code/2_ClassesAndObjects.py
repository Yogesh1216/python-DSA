# # Encapsulation : combining properties and methods related to a object.

# # Object = class object , instance object

# class Test:
#     x = 5   # class object variable
#     def __init__(self):
#         self.a =5   # instance object variable
#         self.b =6
    
#     def f1(self):     # instance method
#         print("instance method")
    
#     @staticmethod
#     def f2():     # 
#         print("hello")
    
#     @classmethod
#     def f3(cls):     # 
#         print(cls.x)
        
# obj = Test()   # we can have multiple instance objects of a class
# obj2 = Test    # one class have only one class object

# obj.f1()
# Test.f3()
# Test.f2()



# print(obj2)
# print(obj2.x)



# class -----------
class Employee:
    def __init__(self,empid=None,name=None,salary=None):
        self.empid = empid
        self.name = name
        self.salary = salary
        
    def set_empid(self,empid):
        self.empid = empid
    def set_name(self,name):
        self.name = name
    def set_salary(self,salary):
        self.salary = salary
    def get_empid(self):
        return self.empid
    def get_name(self):
        return self.name 
    def get_salary(self):
        return self.salary 
    

emp = Employee()
emp.set_empid(10)
emp.set_name("yogesh")
emp.set_salary("120000")
print(emp.get_empid(),emp.get_name(),emp.get_salary())

