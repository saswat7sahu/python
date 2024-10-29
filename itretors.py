#Iterators are methods that iterate collections like lists, tuples, etc.
#  Using an iterator method, we can loop through an object and return its elements
#ython iterator object must implement two special methods, __iter__() and __next__(), collectively called the iterator protocol.
li=[1,2,3,3]
it=iter(li)
print(it.__next__())