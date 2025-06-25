a=[7,10,1,5,3,14,6]
b=0
c=len(a)
d=[]
def mergesort(a,b,c):
    print(a[b:c])
    x=(b+c)//2
    if b==c:
        return 
    else:
        
        mergesort(a,b,x)
        mergesort(a,x+1,c)
        rearrange(a,b,c)
def rearrange(a,b,c):
    d=[]
    j = b
    x=(b+c)//2
    i=x
    print(i)
    while b<x and i<c:
        if a[b]<a[i]:
            d.append(a[b])
            b=b+1
        else:
            d.append(a[i])
            i=i+1
    while i<c:
        d.append(a[i])
        i=i+1
    while b<x:
        d.append(a[b])
        b=b+1
    for h in range(0,len(d)):
        a[j+h]=d[h]
mergesort(a,b,c)
print(a)