# Provide a class that acts, effectively, as the union of a set of ranges. 
# That is to say that ranges can be inserted into said class and then the class can 
# be queried to check if a particular point is in any of the ranges that have been inserted.

# Example:
# Ranges Inserted:

# range 1: 2-5
# range 2: 9-13

# Quried values:
# value1: 0 -> false
# value2: 2 -> True
# value3: 10 -> True