#reverse using slice
a=[2,3,3,1,3,4,43,3,422]
a=a[::-1]
for i in a:
    print(i)
#reverse using pop()
l=[10,220,30,1]
for i in range(len(l)):
    l.insert(i,l.pop())
for i in l:
    print(i)
# reverse uing loop
li=[40,30,10,5]
a,b=0,len(li)-1
while a<len(li)/2:
    temp=li[a]
    li[a]=li[b]
    li[b]=temp
    a+=1
    b-=1
for i in li:
    print(i)