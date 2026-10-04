
class base(object):
    def __init__(self, x):
        self.x = x

class child(base):
    def __init__(self, x,y):
        base.x=x
        self.y=y

    def printWork(self):
        print(base.x)
        print(self.y)

ob=child(1,2)
ob.printWork()
        