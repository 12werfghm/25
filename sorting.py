# a=[10,1,5,4,7]
# def selectionsort(a):
#     for h in range(0,len(a)):
#         b=h
#         for i in range(h,len(a)):
#             if a[b]>(a[i]):
#                 b=i
#         x=a[b]
#         a[b]=a[h]
#         a[h]=x
#         print(a)
#     return a     
# print(selectionsort(a))
a=[7,10,4,5,1]
b = [5,6,2,3,5,7,9,9,4,4,3,1,1]
def bubblesort(a):
    for h in range(0,len(a)):
        for i in range(0,len(a)-1):
            if a[i]>a[i+1]:
                x=a[i]
                a[i]=a[i+1]
                a[i+1]=x
    return a
print(bubblesort(a))
print(bubblesort(b))