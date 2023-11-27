from hw2.vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, company, model, year):
        super().__init__(company, model, year, 4)

    def testDrive(self):
        self.setSpeed(60)

    def park(self):
        self.setSpeed(0)
