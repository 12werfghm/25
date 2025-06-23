a=[10,1,5,4,7]
def sort(a):
    for h in range(0,len(a)):
        b=h
        for i in range(h,len(a)):
            if a[b]>(a[i]):
                b=i
        x=a[b]
        a[b]=a[h]
        a[h]=x
        print(a)
    return a     
print(sort(a))