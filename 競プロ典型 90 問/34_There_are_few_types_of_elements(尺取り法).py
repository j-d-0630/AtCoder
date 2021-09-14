"""
尺取り法
"""
from collections import defaultdict

N,K = map(int,input().split())
A = list(map(int,input().split()))
ans = 0

cr = 0
cnt = 0 # 異なる数字に遭遇した回数

d = defaultdict(int)
for i in range(N): # A[]のi番目の要素から探索開始
  while(cr <= N-1):
    # A[cr]から探索を再開するので計算量が減らせる。それまでの遭遇情報はd[]とcntに保存されている。
    if d[A[cr]] == 0 and cnt == K: # 異なる数字にK回以上遭遇した場合、探索終了し、次のiから探索し直す
      break
    if d[A[cr]] == 0: # 異なる数字に遭遇したが、その回数がK回未満の場合、探索続行
      cnt += 1
    d[A[cr]] += 1 # A[cr]に遭遇した印を付ける
    cr += 1
  
  ans = max(ans,cr - i)
  if d[A[i]] == 1: # i+1番目から探索し直すにあたり、A[i]は遭遇していないことになるので1回だけの遭遇であればcntを1減らす
    cnt -= 1
  d[A[i]] -= 1 # i+1番目から探索し直すにあたり、A[i]とは遭遇していないことになるので、d[A[i]]を1減らす

print(ans)