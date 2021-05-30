N,K = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
A.sort()

for i in range(N):
  if A[i][0] > K:
    break
  K += A[i][1]

print(K)
