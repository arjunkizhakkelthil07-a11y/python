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