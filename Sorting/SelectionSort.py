def selectionSort(arr):
    for i in range(len(arr)):
        last=len(arr)-i-1
        largeindex=findLargeIndex(arr,0,last)
        swap(arr,largeindex,last)


def findLargeIndex(arr,a,b):
    largei=a
    for i in range(b+1):
        if arr[i]>arr[largei]:
            largei=i
    return largei
def swap(arr,x,y):
    temp=arr[x]
    arr[x]=arr[y]
    arr[y]=temp
a=[20,303,-20,0]
selectionSort(a)
for i in a:
    print(i)
