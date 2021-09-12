"""
制約が小さいときは順列全探索
"""
import itertools

N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]

M = int(input())
rum = [[] for _ in range(N+1)]
for _ in range(M):
  x,y = map(int,input().split())
  rum[x].append(y)
  rum[y].append(x)

#走る順の全組み合わせ
pat = list(itertools.permutations(list(range(1,N+1))))

time = 10001
for pat_n in pat:
  flg = 0
  temp_t = 0
  for i in range(N):
    if i > 0:
      if pat_n[i] in rum[pat_n[i-1]]:
        flg = 1
        break 
    temp_t += A[pat_n[i]-1][i] # i経路の走者指定, i経路のタイム
  if flg == 0:
    time = min(time,temp_t)

if time == 10001:
  print(-1)
else:
  print(time)