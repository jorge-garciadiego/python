

"""    A list in python is very similar to the notion of an Array. It is an indexed collection of related objects.

   lists are dynamic in python, they can grow and shrink on demand.

   There is no need to predeclare the size of a list to using it to store any objects

   lists are heterogeneous, we do not need to predeclare the type of the object we are storing - we can mix and match objects of diferent types in one list.

   Lists are mutable, we can change a list ot any time by adding, remmoving or changing objects. """


"""
   A Tuple is an ordered immutable collection of objects
   It is often useful to think of a tuple as a constant list
"""

"""
   A Dictionary is an unordered set of Key/Value pairs


"""

"""
   Set is an unordered set of unique objects

   is a handy data structure for remembering a collection of related objects while ensuring none of the objects are duplicated.

   Sets let us perform unions, intersections and differences.
"""

#lists are always enclosed in square brackets and the objects contained within are always separated by comma
#declaring a list empty -> tacos = []

tacos = ['Tinga', 'Picadillo', 'Pork', 'Shrimp', 'Fish', 'Steak', 'Vegetable']

for main in tacos:
   if main in tacos:
      print(main)
      
#len() reports the size of an object     
print(len(tacos))

#append() methiod to add to an existing list at runtime

tacos.append('Vegan Chorizo')
print(tacos)

#in and not in operators to check whether an object is contained within a collection 

if 'Pork' in tacos:
   print('exists')

if 'Vegan tinga' not in tacos:
   tacos.append('Vegan Tinga')

print(tacos)

#Removing Objects form a list

"""Remove method remove the first occurrence of a specified data value and shrinks the size by one"""

tacos.remove('Steak')
print(tacos)


