#when there is question that given element 1 to n probably we have to appply cyclic sort.
# time complexcity 0(n)
def CyclicSort(arr):
    for i in range(len(arr)):
        if arr[arr[i]-1]!=arr[i]:
            swap(arr,i,arr[i]-1)
def swap(a,x,y):
    temp=a[x]
    a[x]=a[y]
    a[y]=temp

l=[4,2,1,3]
if __name__=="__main__":
    CyclicSort(l)
for i in l:
    print(i)