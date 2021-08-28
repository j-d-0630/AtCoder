N,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

tgt = 0
for i in range(N):
  tgt += abs(A[i] - B[i])

K -= tgt

if K < 0:
  print("No")
else:
  if K % 2 == 0:
    print("Yes")
  else:
    print("No")