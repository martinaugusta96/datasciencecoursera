def quicksort(arr,low,high):
    i=(low-1)
    pivot=arr[high]
    for j in range(low,high):
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return(i+1)


def partition(arr,low,high):
    if low<high:
        pi=partition(arr,high,low)
        quicksort(arr,high,pi-1)
        quicksort(arr,pi+1,low)

arr=[]
for i in range(5):
    arr.append(int(input()))
n=len(arr)
quicksort(arr,0,n-1)
print("Sorted array is :- ")
print(arr)