# Program to illustrate different set operations

# Define the two sets based on the expected output
E = {0, 2, 4, 6, 8}
N = {1, 2, 3, 4, 5}

# Set Union (All elements from both sets) using the | operator
print("Union of E and N is", E | N)

# Set Intersection (Elements common to both sets) using the & operator
print("Intersection of E and N is", E & N)

# Set Difference (Elements in E but not in N) using the - operator
print("Difference of E and N is", E - N)

# Set Symmetric Difference (Elements in either E or N, but not both) using the ^ operator
print("Symmetric difference of E and N is", E ^ N)