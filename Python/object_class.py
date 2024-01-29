class Employee:
    minSalary = 12000
    maxSalary = 120000
    CompanyName = 'Singularixty Corporation'
    def __init__(self, name, salary, department):
        self.__name = name
        self.__salary = salary
        self.__department = department
    def _showdata(self):
        print(f'[{self.__department}] {self.__name} - {self.__salary:,.2f}')
    def modifyname(self, new_name):
        self.__name = new_name
    def modifysalary(self, salary):
        self.__salary = salary
    def get_name(self):
        return self.__name
    
class Programmer(Employee):
    __departmentName = 'โปรแกรมเมอร์'
    
    def __init__(self, name, salary, experience, skill):
        super().__init__(name, salary, self.__departmentName)
        self.__experience = experience
        self.__skill = skill
        self._showdata()
        
    def _showdata(self):
        super()._showdata()  # Call the parent class's _showdata method
        print(f'{self._Programmer__experience}, {self._Programmer__skill}')

class Accounting(Employee):
    __departmentName = 'ฝ่ายบัญชี'
    
    def __init__(self, name, salary, age):
        super().__init__(name, salary, self.__departmentName)
        self.age = age
        self._showdata()

    def _showdata(self):
        super()._showdata()  # Call the parent class's _showdata method
        print(f'{self.age}')

#obj1 = Employee('Singularixty', 5000000,'Chief Executive Officer')
##obj1.modifyname('JohnDoe')
#obj1._showdata()
#print(obj1.get_name())

#obj2 = Employee('JaneDoe', 10284850,'Manager')
#print('Company Name: {}'.format(Employee.CompanyName))
#print('Min Salary {}'.format(Employee.minSalary))
#print(Programmer.minSalary)
ProgrammerObj = Programmer('โปรแกรมเมอร์ 101', 129000, experience='2 Years', skill='Game Development')
AccountingObj = Accounting('นายสมชาย', 19581, age=12)