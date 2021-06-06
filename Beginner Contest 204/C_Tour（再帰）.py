import sys
sys.setrecursionlimit(10000) #再帰回数の上限を10000回に変更

N,M = map(int,input().split())

#都市iから繋がっている都市のリスト
G = [[] for _ in range(N)]
for i in range(M):
  A,B = map(int,input().split())
  G[A-1].append(B-1)

def dfs(v):
  if temp[v]: return #同じ頂点を2度調べないためのreturn
  temp[v] = True
  for vv in G[v]: dfs(vv)

ans = 0
#全ての都市からスタートさせた場合を順番に評価
for i in range(N):
  temp = [False]*N #temp[j]は都市jに到達可能かどうかを表す
  dfs(i)
  ans += sum(temp)

print(ans)
