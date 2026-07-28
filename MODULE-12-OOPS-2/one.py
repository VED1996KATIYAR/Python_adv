#operator overloading
class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth;

v1=Rectangle(5,4)
print(v1.area())
    