input1=int(input("enter first number:"))
input2=int(input("enter second number:"))
def greatest(a,b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "both numbers are equal" 
print("the greatest number is:",greatest(input1,input2))