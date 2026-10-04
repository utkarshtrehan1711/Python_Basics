class car:
    #class Variables
    wheels=4
    def __init__(self):
        print("Default Constructor")

    def __init__(self,color):
        print("Para Constructor")
        self.color=color
        print(color)

    def test(self):
        print("test")

    def setPrice(self,price):
        self.price=price

    def getPrice(self):
        return self.price
c1=car("Blue")
print(c1.wheels)
print(car.wheels)
c1.test()
c1.setPrice(100)
print(c1.getPrice())
