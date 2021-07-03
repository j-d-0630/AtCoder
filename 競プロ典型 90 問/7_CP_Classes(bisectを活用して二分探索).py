import bisect
INF = 2000000000 # 無限大
N = int(input())
A = list(map(int,input().split()))
Q = int(input())
B = [int(input()) for _ in range(Q)]

# 二分探索するためにソートしておく
A.sort(reverse=False)

# 二分探索
for i in range(Q):
  # Q[i]が入る位置を調べる
  pos = bisect.bisect_left(A,B[i])

  Diff1 = INF
  Diff2 = INF
  if pos < N: # Diff1はB[i]とその右側の数値であるA[pos]との差分
    Diff1 = A[pos] - B[i]
  if pos > 0: # Diff2はB[i]とその左側の数値であるA[pos-1との差分
    Diff2 = B[i] - A[pos-1]
  
  #小さい方が解となる
  ans = min(Diff1,Diff2)
  print(ans)