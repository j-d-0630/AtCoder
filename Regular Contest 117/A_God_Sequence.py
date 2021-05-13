# input
a, b = map(int, input().split())
e = [0 for i in range(a + b)]
 
# make "god array"
if a >= b:
    for i in range(a):
        e[i] = i + 1
    for i in range(b - 1):
        e[i + a] = -(i + 1)
    for i in range(a + b - 1):
        e[a + b - 1] -= e[i]
 
if a < b:
    for i in range(a - 1):
        e[i] = i + 1
    for i in range(b):
        e[i + a] = -(i + 1)
    for i in range(a + b):
        if i != a - 1:
            e[a - 1] -= e[i]
 
# output
print(' '.join(map(str, e)))
