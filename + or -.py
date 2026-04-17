i=int(input("enter a number:"))
def check_sign(n):
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    else:
        return "zero"

num = i
print(check_sign(num))
