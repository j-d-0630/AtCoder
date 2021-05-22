N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

A_l = [0]*N
for i in range(N):
  A_l[A[i]-1] += 1

count = 0
for i in range(N):
  now = B[C[i]-1]
  count += A_l[now-1]

print(count)