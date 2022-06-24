'''
OOPS featurs:
==============
Abstraction
Inheritance
Polymorphism
Emcapsulation
'''

class Employee():
    #hike=1.1
    def __init__(self,fname,lname,pay):     #constructor
        self.fname=fname
        self.lname=lname
        self.salary=pay
        self.email=self.fname+'.'+self.lname+'@gmail.com'

    def fullname(self):
        return "{}.{}".format(self.fname,self.lname)

    def appraisal(self):
        self.hike=2
        #print("Hike for the year is : ", self.hike)
        self.salary = int(self.salary*self.hike)

    @classmethod
    def emp_object(cls,emp_str):
        fn,ln,sal=emp_str.split('-')
        return cls(fn,ln,int(sal))            #Employee(fn,ln,sal)

    @staticmethod
    def is_workingday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return "Holiday!"
        else:
            return "Working Day!"

#Inheritance

# class Developer(Employee):
#     def __init__(self,fname,lname,pay,tech):
#         self.fname=fname
#         self.lname=lname
#         self.pay=pay
#         self.email=self.fname+'_'+self.lname+'@yahoo.com'
#         self.tech=tech
#
# dev_1=Developer('Siva','Murugan',100000,'Python')
# print(dev_1.fullname())
# import datetime
# dt = datetime.date(2022, 6, 24)
# print(dev_1.is_workingday(dt))

#print(help(dev_1))

class Manager():
    def info(self):
        print("Data Analyst -python")

    def appraisal(self):
        self.hike=2
        #print("Hike for the year is : ", self.hike)
        self.salary = int(self.salary*self.hike)

class Developer(Employee, Manager):  #multiple Inheritance
    def __init__(self,fname,lname,pay,tech):
        self.tech=tech
        super().__init__(fname,lname,pay)

#Overloading

    def mymethod(self,):
        print("Hello")

    def mymethod(self, name):  #overloading
        print("Hello", name)

    def add_num(self,*args):
        return sum(args)

    def fullname(self, title):  #overriding
        return "{}.{} {}".format(title,self.fname,self.lname)

    def appraisal(self):
        super(Employee, self).appraisal()
        # Manager().appraisal(self)

dev_1 = Developer('Siva', 'Murugan', 100000, 'Python')
dev_2 = Developer('Ramya', 'Karathil', 150000, 'AIML')

print(dev_1.email)
# dev_1.mymethod("Navnath")
# print(dev_1.add_num(1,2,3,4,5,6,7,8))

print(dev_1.fullname(("Mr")))
print(dev_2.fullname(("Mr")))

dev_1.info()
print(dev_1.salary)
dev_1.appraisal()
print(dev_1.salary)
#Method Overloading is not needed in python
#Overloading :two methods in the same nane in a class
# is called overloading. both method varies in number of
# arguments or type of arguments


#Overloading : two method in the same name in a class is called overloading. both method varies in
#number of arguments or type of the arguments