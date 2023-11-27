from abc import ABC, abstractmethod


class Vehicle(ABC):
    __company: str
    __model: str
    __yearRelease: int
    __numWheels: int
    __speed: int

    def __init__(self, company, model, year, numWheels):
        self.__company = company
        self.__model = model
        self.__yearRelease = year
        self.__numWheels = numWheels
        self.__speed = 0
        super().__init__()

    @abstractmethod
    def testDrive(self):
        pass

    @abstractmethod
    def park(self):
        pass

    def getCompany(self):
        return self.__company

    def getModel(self):
        return self.__model

    def getYearRelease(self):
        return self.__yearRelease

    def getNumWheels(self):
        return self.__numWheels

    def getSpeed(self):
        return self.__speed

    def setSpeed(self, speed):
        self.__speed = speed

    def __str__(self):
        if self.__numWheels == 2:
            return f"This moto is a {self.getCompany()} {self.getModel()} {self.getYearRelease()} release;"
        else:
            return f"This car is a {self.getCompany()} {self.getModel()} {self.getYearRelease()} release;"
