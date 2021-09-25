"""

"""
Q = int(input())

A = [0] * (2 *100009) # デッキ：上→下の並び
cl = 100009
cr = 100009

for i in range(Q):
  t,x = map(int,input().split())
  if t == 1:
    cl -= 1
    A[cl] = x
  elif t == 2:
    A[cr] = x
    cr += 1
  elif t == 3:
    print(A[cl + x -1])