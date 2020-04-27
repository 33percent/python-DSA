import datetime
class Employee:
    num_of_emps = 0
    raise_amt = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property   
    def email(self):
        return "{}.{}@company.com".format(self.first, self.last)

    @property
    def full_name(self):
        return "{} {}".format(self.first, self.last)

    @full_name.setter
    def full_name(self,name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @full_name.deleter
    def full_name(self):
        self.first = None
        self.last = None

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
    
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(cur_day):
        if cur_day.weekday() in (5,6):
            return False
        return True
    
    def __repr__(self):
        return "Employee('{}' , '{}' , '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} , {}'.format(self.full_name, self.email )
    
    def __add__(self, other):
        return self.pay + other.pay



Sandeep = Employee(first='Sandeep', last='Khan', pay=10000)
Pawan = Employee(first='Pawan', last='Kalyan', pay=20000)
Jenil = Employee.from_string(emp_str='Jenil-Christo-80000')


#classmethod
Employee.set_raise_amt(1.04)
print(Jenil.email)

#static method 
my_date = datetime.date(2016,7,11)
print(Employee.is_workday(my_date))


class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        self.prog_lang = prog_lang
        super().__init__(first, last, pay)
    raise_amt = 1.10

dev_1 = Developer('sandeep','khan',50000, 'python')
dev_2 = Developer('pawan','kalyan',50000, 'java')
print(dev_1.prog_lang)
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
        
    def print_emps(self):
        for emp in self.employees:
            print(emp.full_name)

Sureka = Manager('Sureka','bla bla', 20000, [dev_1])
Sureka.add_employee(dev_2)
Sureka.remove_employee(dev_1)
Sureka.print_emps()


print(isinstance(Sureka, Developer))
print(issubclass(Developer, Employee))
print(issubclass(Manager, Developer))

#magic methods
print(dev_2.__str__())
print(dev_2.__repr__())
print(dev_1 + dev_2)


# decorators

dev = Developer('sandeep','s',100,'python')

dev.first = 'sandip'
print(dev.full_name)
dev.full_name = 'sandeep s'
del dev.full_name
print(dev.email)
print(dev.full_name)