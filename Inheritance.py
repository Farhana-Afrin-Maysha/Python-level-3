# parent class
class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    # method

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


# sub class 1
class Developer(Employee):
    raise_amt = 1.50

    #   calling parent class
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


# sub class 2
class Manager(Employee):

    #   calling parent class
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    #  adding employee
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    #  remove employee
    def remove_emp(self, emp):
        if emp not in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp  in self.employees:
            print('-->', emp.fullname())

dev_1 = Developer('Farhana', 'Afrin', 50000, 'Python')
dev_2 = Employee('Yousra', 'Afrin', 50000)

mgr_1 = Manager('Saidur', 'Rahman', 90000, [dev_1])

print(mgr_1.email)

mgr_1.add_emp(dev_2)

mgr_1.print_emps()

dev_1.apply_raise()
print(dev_1.pay)
print(dev_1.prog_lang)
print(dev_2.pay)

# isinstance
print(isinstance(mgr_1, Developer))

# subclass or not subclass
print(issubclass(Developer, Employee))