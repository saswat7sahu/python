#list is a collection of elements that may be homogenous or heterogenous. 
# Dynamic is size
#it's a built in data type
#list can use in stack ,queues,
l=[1,2,4,"hi","hlo",True]
print(l[3])
#slicing:  slicing is a powerful feature that allows you to extract a portion of a list.
#list[start:stop:step]
print(l[:3])
#adding an element to list
l.append("dev")
#printing the element
for i in l:
    print(i)
#Array operations
#Merge two list
m=[4,5,6,7,8]
print(l+m)

#built in function
#len(): gives the length of the list
print(len(l))
#max(): give the maximum value of the list.
print(max(m))
#min(): gives the minimum value of the list
print(min(m))
#insert(): to add an element in a specific postion
l.insert(2,"world")
#remove(): to remove a specific  element for list
l.remove(True)
#index() : return the index of element if it's exist.
print(l.index(2))
