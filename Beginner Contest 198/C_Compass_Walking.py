import math

R,X,Y = map(int,input().split())
D = math.sqrt(X**2 + Y**2)

if D == R:
  print(1)
elif D <= 2*R:
  print(2)
else:
  print(math.ceil(D/R))