import math

A,B,K = map(int,input().split())

ans = []
N = A+B
for i in range(N):
  if A == 0:
    ans += "b"
  elif B == 0:
    ans += "a"
  else:
    n = A+B
    #一文字目が"a"となる場合
    if K <= math.factorial(n-1)//(math.factorial(A-1)*math.factorial(B)):
      ans += "a"
      A -= 1
    #一文字目が"b"となる場合
    else:
      ans += "b"
      K -= math.factorial(n-1)//(math.factorial(A-1)*math.factorial(B))
      B -= 1

print("".join(ans))