from operator import truediv

age=int(input("Enter your age "))


if age<0:
    print(age, " Negative Number")


elif age>18:
    print(age, " Adult")
else:
    print(age, " Bachelor")

flag=input("Enter your flag").strip().lower()
if flag=="true":
    ip=True
elif flag=="false":
    ip=False
else:
    print("Flag not recognized")
print(ip)

a=100
b=300
c=765

if a>b and a>c:
    print(a)
elif b>c:
    print(b)
else:
    print(c)
