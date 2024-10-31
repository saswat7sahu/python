#Swap all element in string list
#INput :['hi','iam','no']
#output: ['ih','mai','on']
def reverseli(a):
    a=a[::-1]
    return a

def reverselistElement(arr):
    for i in range(len(arr)):
        arr[i]=reverseli(arr[i])
li=['hi','iam','no']
reverselistElement(li)
for i in li:
    print(i)