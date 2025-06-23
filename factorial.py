a=int(input("Which number"))
b=1
def factorial(a,b):
    if a==b:
        return a
    elif a<1:
        return 1
    else:
        return factorial (a,b+1)*(b)
print(factorial(a,b))