import bisect

N,Q = map(int,input().split())
A = list(map(int,input().split()))

low = [0]*N #採用可能な数の数
for i in range(N):
  low[i] = A[i] - (i+1)

while Q != 0:
  K = int(input())
  idx = bisect.bisect_left(low,K)
  if idx == N: #N番目の数よりも外側の数が解となる場合
    print(A[N-1] + (K - low[N-1])) #A[]の最後尾の数に入れられなかった分の数との差分を足す
  else: #N番目の数内の数が解となる場合
    print(A[idx] - (low[idx] - K + 1))
  
  Q -= 1
