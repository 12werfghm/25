x=1
y=1
z=0
a=int(input("Which number?"))
def fibonacci(a):
   if a==1 or a==0:
      return a
   else: 
      return fibonacci(a-1)+fibonacci(a-2)
      
      
print(fibonacci(a))
# x=int(input("Which number?"))
# def count(x):
#     if x!=0:
#         print(x)
#         count(x-1)
# count(x)