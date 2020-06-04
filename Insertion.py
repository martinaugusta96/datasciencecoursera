def insertion(a):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]

a=[]
for i in range(5):
    a.append(int(input()))
insertion(a)
print(a)