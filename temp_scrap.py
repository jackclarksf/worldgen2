c = 10
e = 5
a = 4

if c > e and e > a:
    print("True!")

if c > e > a:
    print("True")

l = 3, 4
print(l)
print(l[0])

def func_a():
    return 5

def func_b():
    return 8

print(func_a())
lemon = func_a() + func_b()
print(lemon)