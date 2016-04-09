our_tuple = 12, 4
distance_tuple = 14, 2
our_target = 0, 0

print(our_tuple)
print(our_target)
print(distance_tuple)

while distance_tuple > our_tuple:
    a, b = distance_tuple
    a -= 1
    print(a, b)
    distance_tuple = a, b

