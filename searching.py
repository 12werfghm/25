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
    if a[c+e]==b:
        return c+e
    elif e==1 and a[c+e]!=b:
        return -1
    elif a[c+e]>b:
        return search(a,b,c,d-e-1,e)
    else:
        return search(a,b,c+e+1,d,e)
print(search(a,24,c,d,e))
