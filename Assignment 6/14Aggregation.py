class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, emp):
        self.emp = emp

emp1 = Employee("Ali")
dept = Department(emp1)
print(dept.emp.name)
