A="arjun"
print(A)


age=18
print(age)

num=12.5
print(num)


b=[1,2,3,4]
print(b[-1])
b.append(5)
print(b)
b.insert(1,55)
print(b) 
b.pop(4)
print(b)
b.pop(0)
print(b)


c=("apple","orange","cherry")
print(c)
d=list(c)
d.append("mango")
c=tuple(d)
print(c)


age=20
if(age>=18):
    print("you are eligable to vote")
else:
    print("you are not eligable to vote")

age=int(input("enter you age:"))
if(age>=18):
    print("you are eligable to vote")
else:
    print("you are not eligable to vote")

number=int(input("enter a number:"))
if(number % 2==0):
        print(number,"is even")
else:
        print(number,"is odd")

n1=int(input("enter the first number:"))
n2=int(input("enter the 2nd number:"))
n3=int(input("enter the 3rd number:"))
if(n1>n2) and (n1>n3):
     print(n1,"is largest")
elif(n2>n1) and (n2>n3):
     print(n2,"is largest")
else:
     print(n3,"is largest")

