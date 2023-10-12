set_A = {'col', 'mex', 'bol'}
set_B = {'per', 'bol'}
print(set_A)
print(set_B)

# Union

set_C = set_A.union(set_B)
print(set_C)
print(set_A | set_B)

# Intersection

set_D = set_A.intersection(set_B)
print(set_D)
print(set_A & set_B)

# Difference 
set_E = set_A.difference(set_B)
print(set_E)
print(set_A - set_B)
set_z = set_B - set_A
print(set_z)

# Symetric difference
set_F = set_A.symmetric_difference(set_B)
print(set_F)
print(set_A ^ set_B)
