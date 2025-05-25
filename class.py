class employees:
    def __init__(self, fname, lname,age, salary):
      self.fname = fname
      self.lname = lname
      self.age = age
      self.salary = salary
      self.email = fname + '-' + lname + '@company.com'


    def salary_increment(self):
       self.salary += self.salary * 1.04  

emp1 = employees('qurioh', 'max', 25, 50000)
emp2 = employees('kim', 'smith', 30, 50000)

print(emp1.email)
emp1.salary_increment()
print("Updated Salary for emp1:", emp1.salary)
print(emp2.email)