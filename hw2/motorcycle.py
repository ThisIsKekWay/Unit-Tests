from hw2.vehicle import Vehicle


class Motorcycle(Vehicle):
    def __init__(self, company, model, year):
        super().__init__(company, model, year, 2)

    def testDrive(self):
        self.setSpeed(75)

    def park(self):
        self.setSpeed(0)
