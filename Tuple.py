#Tuple is an immutable, ordered collection of elements.We can't change the elements of a tuple.
t=(2,45,5,3,3)
for i in t:
    print(i)
#if we want to change it's value.typecast it's value to another datatypes like list.
#Aslo we can create a new tuuple out of this.change the value according to this.
nt=t[:2]+(8,)+t[4:]

