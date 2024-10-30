def repeated(arr):
    repeatedlist=[]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j] and arr[j] not in repeatedlist:
                repeatedlist.append(arr[j])
    return repeatedlist 
a=[10,30,10,2,0,2,-20,-20]
b=repeated(a)
for i in b:
    print(i)