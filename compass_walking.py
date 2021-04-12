import math

def function(R,X,Y):
    distance = math.sqrt(X**2 + Y**2)

    tmp = int(distance/R)

    if distance == R:
        rslt = 1
    elif distance < 2*R:
        rslt = 2
    else:
        rslt = math.ceil(distance/R)

    return rslt

tmp = input()
tmp2 = tmp.split()
R = int(tmp2[0])
X = int(tmp2[1])
Y = int(tmp2[2])

ans = function(R,X,Y)
print(ans)