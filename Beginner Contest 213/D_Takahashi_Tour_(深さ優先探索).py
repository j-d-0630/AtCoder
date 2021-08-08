"""
木のオイラーツアー
"""
import sys
sys.setrecursionlimit(300000)

N = int(input())
G = [[] for _ in range(N+1)]
for i in range(N-1):
  A,B = map(int,input().split())
  G[A].append(B)
  G[B].append(A)

for i in range(N+1):
  G[i].sort()

ans = []
def dfs(crr,pre):
  ans.append(crr)
  for nxt in G[crr]:
    if nxt != pre: # 一つ前の都市と同じ場合はスキップ（前の都市から来てるので必ず前の都市が行先候補リストには入っており、これをスキップしたい）
      dfs(nxt,crr) # 行ったことがない町がある限りは再帰で次の都市へ移動し続ける
      ans.append(crr) # 行先が無くなったので一つ前の都市をappend

dfs(1,-1)
print(*ans)