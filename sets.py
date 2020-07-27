# Create an empty set
s = set()

# add to the set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)
print(s)
print(f"The set has {len(s)} values")

# sets only have unique values. Even if you add multiple duplicate values, only one will be in the set.

# .remove allows us to remove from the set. len stands for length and tells the number of values in the set. need to nest it in {}
s.remove(2)
print(s)

# note how this command has an f for funtction which is what allows the program to pull the len within the {}
print(f"the set now has {len(s)} values")
