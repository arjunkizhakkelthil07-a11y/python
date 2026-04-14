a=int(input("enter the amount:"))
balance=1000
if(a>balance):
    print("insufficent balance")
else:
    print("withdraw")
    print("remaining balance",balance-a)
