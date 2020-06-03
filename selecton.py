def selection(a):
    small=min(a)
    b.append(small)
    a.remove(small)

a=[]
b=[]
for i in range(5):
    a.append(int(input()))
for i in range(5):
    selection(a)
print(b)
