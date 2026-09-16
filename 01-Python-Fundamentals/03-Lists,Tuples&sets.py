"""
Topic: [Lists, Tuples, and Sets]
"""

# Lists = "A list stores multiple items in a ordered collection. Lists are mutable, Lists are defined using square brackets []."     
#       Key points:
        # Lists are ordered
        # Lists are mutable
        # Lists can contain duplicate items
        # use [] to define a list

 # List example:
list_1 = [1, 2, 3, 4, 5]
list_2 = ['apple', 'banana', 'cherry'] 
list_1.extend(list_2) # extend() method adds the elements of list_2 to list_1
list_1.remove('apple')
list_1.insert(0,'apple') 
print(list_1) 


# tuples = it is similar to a list but it is immutable. Tuples are defined using parentheses ().

     # Key points:
        # Tuples are ordered    
        # Tuples are immutable
        # allow duplicate items
        # Use () to define a tuple

# Tuples example:

tuple_1 = (1, 2, 3, 4, 5)
print(tuple_1[0])

# Sets = "A set is an unordered collection of unique items. Sets are mutable, but they do not allow duplicate items. Sets are defined using curly braces {}."

    # Key points:
        # Sets are unordered
        # Sets are mutable
        # Sets do not allow duplicate items
        # Use {} to define a set
# Sets example:
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 5, 6, 7, 8}
print(set_1.union(set_2))           #{1, 2, 3, 4, 5, 6, 7, 8}
print(set_1.intersection(set_2))    #{4, 5}
print(set_1.difference(set_2))      #{1, 2, 3}