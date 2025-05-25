class Employee:
    def __init__(self):
        self.name = "John"
        self._salary = 50000
        self.__ssn = "123-45-6789"

emp = Employee()
print(emp.name)        
print(emp._salary)      
print(emp._Employee__ssn) 