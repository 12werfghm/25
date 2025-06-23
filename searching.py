# a=[9,4,6,3,7]
# b=int(input("Search for what?"))
# def search(a,b):
#     for i in range(0,len(a)):
#         if a[i]==b:
#             return i
#     return -1
# print(search(a,b))
a=[1,5,10,13,25]
c=0
d=len(a)
e=d
def search(a,b,c,d,e):  
    print(a[c:d])
    e=e//2
    if a[c]==b:
        return c
    elif a[c]>b:
        search(a,b,c,d-len(a)+e,e)
    else:
        search(a,b,c+len(a)-e,d,e)
print(search(a,13,c,d,e))
