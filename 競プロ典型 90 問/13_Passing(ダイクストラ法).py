"""
重み付きグラフにおける各頂点への最短経路はダイクストラ法
"""
from heapq import heappush, heappop

N,M = map(int,input().split())
G = [[] for _ in range(N+1)]
for i in range(M):
  A,B,C = map(int,input().split())
  G[A].append([B,C]) # [隣接しているノード, コスト]
  G[B].append([A,C])

INF = 1000000009
def dijkstra(s,n): # (始点, ノード数)
  dist = [INF] * n
  hq = [[0,s]] # [distance, node]
  dist[s] = 0
  seen = [False] * n # ノードが確定済かどうか
  while hq:
    v = heappop(hq)[1]
    seen[v] = True
    for to, cost in G[v]: # ノードvに隣接しているノードに対して
      if seen[to] == False and dist[v] + cost < dist[to]: # 最短距離が更新できる場合
        dist[to] = dist[v] + cost
        heappush(hq, [dist[to],to])
  return dist # sから各ノードへの最短距離のリスト

dist1 = dijkstra(1,N+1)
distN = dijkstra(N,N+1)

for i in range(1,N+1):
  ans = dist1[i] + distN[i]
  print(ans)