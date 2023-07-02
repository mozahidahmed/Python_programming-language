#01.
# set of integers
my_set = {1, 2, 3}
print(my_set)   # Output: {1, 2, 3}

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)   # Output: {'Hello', 1.0, (1, 2, 3)}

#02.Add 
my_set = {1, 3}
print(my_set) # Output: {1, 3}

my_set.add(2)
print(my_set) # Output: {1, 2, 3}

my_set.update([4, 5, 6])
print(my_set) # Output: {1, 2, 3, 4, 5, 6}

#Remove 
my_set = {1, 3, 4, 5, 6}
my_set.remove(6)
print(my_set)    # Output: {1, 3, 5}



