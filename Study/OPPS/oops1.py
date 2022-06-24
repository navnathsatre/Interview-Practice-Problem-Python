#oops => Objected oriented programming
# class
# object
# methods (function)
#     object
#     class
#     static
# attribute (variable)
#     object attr
#     class attr

class Employee():
    def __init__(self, fname, lname, pay):  # constructor
        self.fname = fname
        self.lname = lname
        self.salary = pay
        self.email = self.fname+'.'+self.lname+'@gmail.com'

    def fullname(self):
        return "{}.{}".format(self.fname,self.lname)


emp_1 = Employee("Navnath", "Satre",  40000)
emp_2 = Employee("Levin", "Lenus", 60000)

print('EMP1: ', emp_1.fullname())
print('EMP2: ', emp_2.fullname())
