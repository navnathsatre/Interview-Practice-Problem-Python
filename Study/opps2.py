

class Employee():
    hike = 1.1
    def __init__(self, fname, lname, pay):     #constructor
        self.fname = fname
        self.lname = lname
        self.salary = pay
        self.email = self.fname+'.'+self.lname+'@gmail.com'

    def appraisal(self):
        # self.hike=hike
        self.salary = int(self.salary*self.hike)


emp_1 = Employee('Raghul','Ramesh', 50000)
emp_2 = Employee('Levin','Lenus', 60000)

emp_1.hike=1.5
print(emp_1.salary)
emp_1.appraisal()
print(emp_1.salary)

print(emp_2.salary)
emp_2.appraisal()
print(emp_2.salary)




