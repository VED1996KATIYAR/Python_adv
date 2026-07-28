class Vehicle:
    company="XYZ123"
    def __init__(self,wheels,seats,mileage):
        print("This is the init of the vehicle")
        self.wheels=wheels
        self.seats=seats
        self.mileage=mileage
    def getdetails(self):
        print(f"The no of wheels is {self.wheels} and the no of seats is {self.seats} ans the mielage is {self.mileage}")

# vehicle1=Vehicle(4,7,30)
# vehicle1.getdetails()

class Car(Vehicle):
    def __init__(self,carname,type,sunroof,wheels,seats,mileage):
        self.carname=carname
        self.type=type
        self.sunroof=sunroof
        Vehicle.__init__(self,wheels,seats,mileage)

    def getdetails1(self):
        print(f"The carname is {self.carname} the type is {self.type} and the sunroof is {self.sunroof} the no of wheels is {self.wheels} the no of seats are {self.seats} and the no of mielage is {self.mileage}")

car1=Car("XUV500","AUTOMATIC","AVAILABLE",4,7,30)
car1.getdetails1()
        