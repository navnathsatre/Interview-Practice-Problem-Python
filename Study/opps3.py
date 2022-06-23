class Employee():
    hike = 1.1

    def __init__(self, fname, lname, pay):  # constructor
        self.fname = fname
        self.lname = lname
        self.salary = pay
        self.email = self.fname + '.' + self.lname + '@gmail.com'

    def fullname(self):
        return "{}.{}".format(self.fname, self.lname)

    def appraisal(self):
        self.hike = 2
        # self.hike=hike
        self.salary = int(self.salary * self.hike)

    @classmethod
    def emp_object(cls, emp_str):
        fn, ln, sal = emp_str.split('-')
        return cls(fn, ln, int(sal))    # Employee(fn, ln, sal)

    @staticmethod
    def is_workingday(day):
        if day.weekday() == 5 or day.weekday == 6:
            return "Holiday!"
        else:
            return "Working Day!"


str1 = 'Malini-Sekar-100000'
str2 = 'Tharani-Sekar-100000'

# fn, ln, sal = str1.split('-')
# emp_1 = Employee(fn,ln, sal)

emp_1 = Employee.emp_object(str1)

# fn, ln, sal = str2.split('-')
# emp_2 = Employee(fn, ln, sal)

emp_2 = Employee.emp_object(str2)

import datetime
dt = datetime.date(2022, 6, 23)
print(Employee.is_workingday(dt))

# emp_1.hike=1.5
# print(emp_1.salary)
# emp_1.appraisal()
# print(emp_1.salary)
#
# print(emp_2.salary)
# emp_2.appraisal()
# print(emp_2.salary)

# print('{}, {}'.format(emp_1.fullname(), emp_2.fullname()))
