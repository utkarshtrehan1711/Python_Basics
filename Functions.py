def test():
    print("test")

test()

def test2(a):
    print(a+10)

test2(22)

def getCountryName(name="India"):
    print(name)
getCountryName()
getCountryName("UK")
getCountryName("USA")
getCountryName(345)
getCountryName(88.55)

def getNames(list):
    for item in list:
        print(item)

getNames(["India","USA","Germany"])

def sumNumbers(num1,num2):
    return num1+num2

c=sumNumbers(10,2)
print(c)

def country(count):
    if count=="India":
        return "New Delhi"
    elif count=="USA":
        return "America"
    elif count=="Germany":
        return "Sydeny"
    else:
        return "unknown"


print(country("USA"))


def getstudentsmarks(**args):
    for key, value in args.items():
        print("%s==%s"%(key,value))

getstudentsmarks(Utkarsh=98,Akshit=90,Meena=99)
getstudentsmarks(key="Apple",seller="Baskin")
