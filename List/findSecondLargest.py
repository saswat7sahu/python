#find the second largest element in list
def findSecondLargest(arr):
    largest=SecondLargest=0
    for i in range(len(arr)):
        if arr[i]>largest:
            SecondLargest=largest
            largest=arr[i]
        elif arr[i]>SecondLargest and arr[i] !=0:
            SecondLargest=arr[i]
    return SecondLargest
a=[20,1,2,3,4]
print(findSecondLargest(a))