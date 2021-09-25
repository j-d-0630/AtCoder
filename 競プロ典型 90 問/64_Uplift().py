"""
隣接区画のみが答えに影響する
"""
N,Q = map(int,input().split())
A = list(map(int,input().split()))

ans = 0
B = [0] * N # 最後尾は空欄として使う
for i in range(N-1):
  B[i] = A[i+1] - A[i]
  ans += abs(B[i])

for i in range(Q):
  L,R,V = map(int,input().split())
  L -= 1
  R -= 1
  mae = abs(B[L-1]) + abs(B[R])
  if L >= 1:
    B[L-1] += V
  if R <= N-2:
    B[R] -= V
  ato = abs(B[L-1]) + abs(B[R])
  ans += (ato - mae)
  print(ans)