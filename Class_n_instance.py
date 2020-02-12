class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    # method

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

# instance variable
emp_1 = Employee('Farhana', 'Afrin', 50000)
emp_2 = Employee('Yousra', 'Afrin', 50000)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
