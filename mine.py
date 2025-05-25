class cars:
    def __init__(self, mname, nplate, cost, date):
        self.mname = mname
        self.nplate = nplate
        self.cost = cost
        self.date = date
    
car1 = cars('BMW', 'KDG', 2500000, 10/5/2010)
car2 = cars('Benz', 'KCA', 3000000,12/5/2010)

print(car1.nplate)
print(car2.cost)