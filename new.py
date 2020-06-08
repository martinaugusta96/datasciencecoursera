'''secret_number=3
print("You have 3 chances to kill it \n")
for i in range(3):
        a=int(input(f"Chance {i+1} What number do u guess it might be...???  "))
        if a==secret_number:
                print(f"Ur guess {a} was correct")
                break
        else:
                i+=1
else:
   print("Better luck next time !!! ")
44444444444444444444444444444444444444444444
c=[5,2,5,2,2]
for cont in  c :
        emp=""
        for i in range(cont):
                emp+="*"
        print(emp)
33333333333333333333333333333333333333333333333333333333333333333333333333333333
list = [2,4,2,8,5]
max=0
for i in list:
     if i>max:
           max=i
           i+=1
print(max)
333333333333333333333333333333333333333333333333333333333333333333333333333333333
mat1=int [[1,2,3],[3,4,5],[5,6,7]]
mat2=int [[1,2,3],[3,4,5],[5,6,7]]
print(mat1*mat2)
2222222222222222222222222222222222222222222222222222222222222222222222222222
list = [2,4,6,8]
num=int(input("Ehter the number :"))
for  i in range(4):
        while list[i]<num:
                i+=1
        else:
                list.insert(i,num)
                break
print(list)
3333333333333333333333333333333333333333333333333333333333333333333333333333333333
list=[]
b=int(input("Enter length of list : "))
for i in range(b):
        a=int(input(f"Enter the number {i+1}  "))
        list.append(a)
print(f"Initial list is {list}")
for i in range(b):
        for y in range(i+1,b-1):
                if list[i]==list[y]:
                        list.remove(y)
                y+=1
        i+=1
print(list)

N = [6,5,28]
s=0
for j in range(3):
    for i in range(1,N[j]):
        if N[j] % i==0:
            s = s + i
    if s == N[j]:
        print(f"Yes {s}")
        s=0
    else:
        print(f"NO {s}")
        s=0
######################LR#######################
list=[]
list1=[]
list2=[]
list3=[]
list4=[]
sq=[]
s1=0
s2=0
s3=0
s4=0
s5=0
a=int(input("Enter the number of entries :- "))
for i in range(a):
        b=int(input(f"Enter value {i+1} of independent variable value :- "))
        list.append(b)
        s1+=list[i]
        c=int(input("Enter value of that dependent variable :- "))
        list1.append(c)
        s2+=list1[i]
m1=s1/a
m2=s2/a
for i in range(a):
        s=list[i]-m1
        s3+=s
        list2.append(s)
        s5+=s*s                                 #ssx
        list3.append(list1[i]-m2)
        s4+=list2[i]*list3[i]                   #ssxy
        list4.append(s4)
nv=s4/s5
nv2=m2-nv*m1
predict=int(input("Enter the independent value :- "))
k=nv2+nv*predict
print(f"The predicted dependent value is :- {k}")

#RECursion
def fact(a):
        if a>=1:
                return a*fact(a-1)
        else:
                return 1
a=int(input("ENter a num:- "))
print(f"Factorial of {a} is ",fact(a))

22222222222222222222222222222222222222222222222222222222222222222

class hand():
    def __init__(self,one,two,three):
        self.first=one
        self.second=two
        self.third=three
myset=hand("We","are","best")
myset1=hand("e","ar","bes")
print(myset.first,myset1.second,myset.third)
33333333333333333333333333333333333333333333333
class node():
    def __init__(self,data):
        self.data=data
        self.next=None
class ll():
    def __init__(self):
        self.head=None
    def cr8():
        a=1
        llist=ll()
        llist = node(a)
        llist.data=int(input(f"Enter the data"))
        b=input("DO you want to extend the linked list ?")
        c=str(b.lower())
        if c=='yes':
            a+=1
            a=node(a)
            llist.next=a
            a.data=int(input("Enter the data :- "))
while(a.next!=None):
    pri

import math
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# Allocates a new node with given data
def newNode(data):
    new_node = Node(data)
    new_node.data = data
    new_node.next = None
    return new_node
# Function to insert a new node at the
# end of linked list using recursion.
def insertEnd(head, data):
    # If linked list is empty, create a
    # new node (Assuming newNode() allocates
    # a new node with given data)
    if (head == None):
        return newNode(data)

        # If we have not reached end,
    # keep traversing recursively.
    else:
        head.next = insertEnd(head.next, data)
    return head
def traverse(head):
    if (head == None):
        return
    # If head is not None, print current node
    # and recur for remaining list
    print(head.data, end=" ");
    traverse(head.next)
# Driver code
if __name__ == '__main__':
    head = None
    head = insertEnd(head, 6)
    head = insertEnd(head, 8)
    head = insertEnd(head, 10)
    head = insertEnd(head, 12)
    head = insertEnd(head, 14)
    traverse(head)

import math
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
def nnode(data):
    n_node=node(data)
    n_node.data=data
    n_node.next=None
    return n_node
def ins(head,data):
    if (head==None):
        return nnode(data)
    else:
        head.next=ins(head,data)
def tra(head):
    if (head==None):
        return
    print(head.data,end="")
    tra(head.next)
if __name__ == '__main__':
    head=None
    head=ins(head,4)
    head = ins(head, 4)
    head = ins(head, 4)
    head = ins(head, 4)
    tra(head)

IIIIIIIIIIIIIIIMMMMMMMMMMMMMMMMMMPPPPPPPPPPPPPPPPPP
    from sklearn import metrices, cross_validation
    import tensorflow as tf
    from tensorflow.contrib import learn

    def main(unused_argv):
        grep=learn.dataset.load_dataset("lication of file")
        x_train,x_test, y_train, y_test=cross_validation.train.test.split(grep.data, grep.target, test_size=0.2,random_state=42)
        classifier=learn.DNNClassifier(hidden_units=[10,20,30], n_class=3)
        classifier.fit(x_train,y_train,steps=200)
        score=metrices.accuracy_score(y_test,classifier.predict(x_test))
        print(f"accuracy : {0:f}".format(score))
444444444444444444444444444444444444444444444444444444444444444444444444444444444444
list=[1,11,3,0,15,5,2,4,10,7,12,6]
m=0
i=0
j=0
for i in range(len(list)):
    for j in range(len(list)):
        if list[i]-list[j]>m:
           m=list[i]-list[j]
           a=i
           b=j
print(list[a],list[b])
555555555555555555555555555555555555555555555555555555555555555555555555555555555555555

list1=[]
list2=[]
list3=[]
ml=[1,2,3,4,5]
l=3
n=5
sum=0
max=0
i=0
for i in range(5):
    max+=ml[i]
eq=max/l
i=0
sum1=0
sum2=0
sum3=0
for i in range(5):
    sum1+=ml[i]
    if sum1<=eq+1:
        list1.append(ml[i])
    elif sum1>(2*eq)+1:
        list3.append(ml[i])
    else:
        list2.append(ml[i])
print(list1)
print(list2)
print(list3)
for i in range(len(list1)):
    sum+=list1[i]
print(sum)
66666666666666666666666666666666666666666666666666666666666666666
#2
list=[6,5,28]
s=0
#a=int(input("Enter the number of numbers:- "))
#for i in range(a):
#    b=int(input(f"Enter the number {i+1}:- "))
 #   list.append(b)
for j in range(3):
    for i in range(1,list[j]):
        if list[j]%i==0:
            s+=i
    if list[j]==s:
            print("Yes")
            s=0
    else:
            print("No")
            s=0
a=234
b=int(input("Enter your guess"))
if b==a:
    print("Perfect guess")
elif b<244 and b>224:
    print("Close enough")
else:
    print("Wrong.")
888888888888888888888888888888888888888888888888888888

import statistics
list1=[]
list2=[]
list3=[]
final=[]
a=int(input())
for i in range(a):
    list1.append(input())
    i+=1
int(list1)
print(list1)
i=0
for i in range(a):
    list2.append(input())
    i+=1
int(list2)
i=0
for i in range(a):
    list3.append(list2[i]/list1[i])
    i+=1
int(list3)
i=0
ans=0
for i in range(a):
    for j in range(a):
        var=list3[i]*list1[j]
        if i!=j and var<list2[j]:
            final.append(list3[i])
print(statistics.mode(final))
#123456789098765432134567890987654321234567890-09876543234567890-09876543
'''













