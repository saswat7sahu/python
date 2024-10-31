#Python Set is an unordered collection of data types that is iterable, mutable, and 
# has no duplicate elements.
#Once a set is created, we cannot change its items, but we can remove items and add new items.
myset={"hi","hlo","me"}
newSet={"namste","namaskar"}
#adding value to set
myset.add("hye")
#removing value from set
myset.remove("me")
#updating value in set
myset.update(newSet)
#----------------------------------------------------------------------------------------------------------
  
  #set operation
# intersection method used to find the item that are present in both the set
set1={"new","type"}
set2=myset.intersection(set1)
#we can do the same intersection using & operator
set3= myset & set1
#intersection_update() method will also keep ONLY the duplicates,
#  but it will change the original set instead of returning a new set.
set1.intersection_update(newSet)
# union() method is used for union operation that is used to add one or more set .
myset.union(set1)
