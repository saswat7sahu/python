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
#LISTING THE ELEMENT
for k in dict:
    print(k, dict[k])
# Iterating over values
for value in dict.values():
    print(value)
#built in function in dictionary
#keys(): return all keys in the dicctionry
print(dict.keys())
# values(): return the values of all the element of the dictionary
print(dict.values())

