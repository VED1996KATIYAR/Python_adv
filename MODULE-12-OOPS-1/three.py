class Vehicle:
    company="XYZ company"
    def __init__(self,wheels,seats,mielage):
        print("The details of the vehicles are")
        self.wheels=wheels
        self.seats=seats
        self.mielage=mielage
    def getdetails(swlf):
        print(f"The no of wheels is {swlf.wheels} the no of seats are {swlf.seats} the mielage of the vehicle is {swlf.mielage}")

v1=Vehicle(4,7,30)
v1.getdetails()

class car(Vehicle):
    def __init__(self, model,type,sunroof,wheels, seats, mielage):
        self.model=model
        self.type=type
        self.sunroof=sunroof
        Vehicle.__init__(self,wheels,seats,mielage)
    

    def getdetails(swlf):
        print(f"The model of car is {swlf.model} the type is {swlf.type} the sunroof is {swlf.sunroof} the wheels are {swlf.wheels} the seats are {swlf.seats} the mielage is {swlf.mielage}")

v2=car("XUV500","automatic","not available",4,7,30)
v2.getdetails()

class electric_car(car):
    def __init__(self, model,type,sunroof,wheels, seats, mielage,batterylife,charging_time):
        self.batterylife=batterylife
        self.charging_time=charging_time
        car.__init__(self,model,type,sunroof,wheels,seats,mielage)
    

    def getdetails(swlf):
        print(f"The model of car is {swlf.model} the type is {swlf.type} the sunroof is {swlf.sunroof} the wheels are {swlf.wheels} the seats are {swlf.seats} the mielage is {swlf.mielage} the battery life is {swlf.batterylife} the charging time is {swlf.charging_time}")

v3=electric_car("XUV500","automatic","not available",4,7,30,"5years","30minutes")
v3.getdetails()