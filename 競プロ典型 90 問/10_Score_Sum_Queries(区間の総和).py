"""
区間の総和は予めメモしておく
"""
N = int(input())
C = [0]
P = [0]
for _ in range(N):
  c,p = map(int,input().split())
  C.append(c)
  P.append(p)

Q = int(input())
L = []
R = []
for i in range(Q):
  l,r = map(int,input().split())
  L.append(l)
  R.append(r)

# クラスごとの累積和を求める
sum1 = [0]*100001
sum2 = [0]*100001
for i in range(1,N+1):
  sum1[i] = sum1[i-1]
  sum2[i] = sum2[i-1]
  if C[i] == 1:
    sum1[i] += P[i]
  else:
    sum2[i] += P[i]

for i in range(Q):
  ans1 = sum1[R[i]] - sum1[L[i]-1]
  ans2 = sum2[R[i]] - sum2[L[i]-1]
  print(ans1,ans2)