class Vehicle:
    comapny="XYZ Motors"
    def __init__(self,n_wheels,n_seats,mileage):
        print("init of vehicle")
        self.n_wheels=n_wheels
        self.n_seats=n_seats
        self.mileage=mileage

    def get_details(self):
        return f"This vehicle has {self.n_wheels} wheels ,{self.n_seats} seats and provide a mileage of {self.mileage}"

# v1=Vehicle(4,7,30)
# print(v1.get_details())

class Car(Vehicle):
   def __init__(self,car_type,drive_type):
       print("init of car")
       self.car_type=car_type
       self.drive_type=drive_type
       Vehicle.__init__(self,4,7,30)

#Car class inherits the vehicle class
#Car class is class child class/derived class
#Vehicle class is called Parent class/base class

# c1=Car(4,5,20)
# print(c1.get_details())

c1=Car("XUV","MANUAL")
print(c1.car_type)
print(c1.drive_type)
print(c1.get_details())
print(c1.__dict__)