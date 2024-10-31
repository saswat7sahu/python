#A dictionary is a built-in data type that represents a collection of key-value pairs.
#Each key-value pair in a dictionary maps the key to its corresponding value.
#Dictionaries are unordered, mutable, and indexed by keys, which means you can change their content, but you cannot access items by their position.
dict={ 'name':"Saswat",
      'age':22,
      'country':'india'}
# Accessing elements
print(dict['name'])
print(dict.get('age'))
#adding a new element
dict['city']='dhenkanal'
dict.update({"dob": "1 jan"})
#LISTING THE ELEMENT
for k in dict:
    print(k, dict[k])
# Iterating over values
for value in dict.values():
    print(value)
#built in function in dictionary
#copy() is used to copy the dictionary
newdict=dict.copy()
#keys(): return all keys in the dicctionry
print(dict.keys())
# values(): return the values of all the element of the dictionary
print(dict.values())
#item() method return each item in dictionary
print(dict.items())
# removing the element from the dictionary
dict.popitem()
#popitem will remove the last element from the list
#pop() is used to remove a particular value from the list
dict.pop("dob")
# empty() is used to empty the dictionary
dict.empty()
#del is used to delete the dictionary
del dict