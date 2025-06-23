# a=int(input("Which number?"))
# b=1
# c=int(input("How much to add?"))
# def add(a,b,c):
#     if b==c:
#         return a+b
#     else:
#         return add(a,b+1,c)
# print(add(a,b,c))
a=int(input("First number"))
b=int(input("Second number"))
def multiply(a,b):
    if b==1:
        return a
    else:
        return multiply(a,b-1)+a
print(multiply(a,b))