def bubble(a):
    i=0
    j=1
    for i in range(5):
        for j in range(5):
            if a[i]>a[j] and i<j:
                a[i],a[j]=a[j],a[i]
a=[]
for i in range(5):
    a.append(int(input()))
i=0
for i in range(5):
    bubble(a)
print(a)