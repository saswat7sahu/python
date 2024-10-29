# time complexcity 0(n^2)
def insertion(arr):
    for i in range(len(arr)-1):
        ele=i+1
        while ele>0 and arr[ele-1]>arr[ele]:
            swap(arr,ele,ele-1)
            ele-=1
def swap(arr,a,b):
    temp=arr[a]
    arr[a]=arr[b]
    arr[b]=temp
a=[10,30,50,20,10,0,-10]
insertion(a)
for i in a:
    print(i)