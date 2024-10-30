#list of prdodcut excluding the duplicates in the list
def ListProduct(arr):
    prli=[]
    for i in arr:
        if i not in prli:
            prli.append(i)
    return product(prli)
def product(a):
    res=1
    for i in a:
        res*=i
    return res
arr=[3,4,3,2,5,2,10]
print(ListProduct(arr))