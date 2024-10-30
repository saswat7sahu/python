def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(1,len(arr)-i):
            if arr[j-1]>arr[j]:
                swap(arr,j-1,j)
                j+=1
            else:
                j+=1
            
def swap(arr,x,y):
    temp=arr[x]
    arr[x]=arr[y]
    arr[y]=temp

a=[20,10,50,0,-10,100,0]
bubbleSort(a)
for i in a:
    print(i)