from sys import stdin
input = stdin.readline

N = int(input())
G = [[] for _ in range(N)]
for i in range(N-1):
  A, B = map(int,input().split())
  A -= 1
  B -= 1
  G[B].append(A)
  G[A].append(B)


def getdist(start:int):
  dist = ["INF"] * N
  # 幅優先探索により、最短距離を計算
  Q = []
  Q.append(start)
  dist[start] = 0

  while len(Q) != 0:
    pos = Q.pop(0)
    for j in G[pos]:
      if dist[j] == "INF":
        dist[j] = dist[pos] + 1
        Q.append(j)

  return dist


# 頂点1からの最短距離を求める
dist1 = getdist(0)
max_v = -1 # 最大距離の暫定値
maxid1 = -1 #最大値のnode番号
for i in range(N):
  if max_v < dist1[i]:
    max_v = dist1[i]
    maxid1 = i

# maxid1からの最短距離を求める
dist2 = getdist(maxid1)
max_v2 = max(dist2)

ans = max_v2 + 1
print(ans)