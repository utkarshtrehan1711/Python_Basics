class base1(object):
    def __init__(self):
        self.str1="Base1"
        print("Parent 1")

class base2(object):
    def __init__(self):
        self.str2="Base2"
        print("Parent 2")

class child(base1,base2):
    def __init__(self):
        self.str3="Child"
        print("Child 1")
        base1.__init__(self)
        base2.__init__(self)

    def printstring(self):
        print(self.str1)
        print(self.str2)

obj = child()
obj.printstring()