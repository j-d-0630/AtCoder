"""
隣接リストでグラフを表現
"""
N,M = map(int,input().split())
G = [[] for _ in range(N+1)]

# 隣接リスト
for _ in range(M):
  a,b = map(int,input().split())
  if a > b:
    G[a].append(b)
  else:
    G[b].append(a)

ans = 0
for g in G:
  if len(g) == 1:
    ans += 1

print(ans)