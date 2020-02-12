class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    # method

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # cls is default class variable to take as an argument by @classmethod
    # classmethod can b used as a constructor
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # statimethod dont acts as an instance or class
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or  day.weekday() == 6:
            return False
        return True

# instance variable
emp_1 = Employee('Farhana', 'Afrin', 50000)
emp_2 = Employee('Yousra', 'Afrin', 50000)

emp_str_1 = 'Maysha-Afrin-90000'
emp_str_2 = 'Mahfuz-Ali-96000'
emp_str_3 = 'Anha-Afrin-90000'

new_emp_1 = Employee.from_string(emp_str_1)


print(Employee.num_of_emps)

print(emp_1.__dict__)

Employee.set_raise_amt(6.00)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

print(new_emp_1.first)
print(new_emp_1.last)

# implementation of class method
import datetime
my_date = datetime.date(2020, 11, 2)

print(Employee.is_workday(my_date))