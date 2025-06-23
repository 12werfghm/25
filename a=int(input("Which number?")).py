a=int(input("Which number?"))
b=1
def add(a,b):
    if b==int(input("How much to add?")):
        return a+b
    else:
        return add(a,b+1)
print(add(a,b))