"""
有向グラフを互いに到達可能なグループに分けることを強連結成分分解(SCC)という
step1：深さ優先探索をして、帰りがけ順に番号を記録
step2：辺の向きを全て反転させ、番号の大きい順に深さ優先探索する
"""
import sys
sys.setrecursionlimit(10 ** 9)

used = [False]*(100001)
G = [[] for _ in range(100001)]
H = [[] for _ in range(100001)]
I = [] # 深さ優先探索の結果

def dfs(pos:int): # 深さ優先探索の結果をIに記録
  used[pos] = True
  for i in G[pos]:
    if used[i] == False:
      dfs(i)
  I.append(pos)

def dfs2(pos:int): # posに帰ってこれるグループが何個の頂点から構成されるかをcntsに記録
  used[pos] = True
  global cnts
  cnts += 1 
  for i in H[pos]:
    if used[i] == False:
      dfs2(i)


N,M = map(int,input().split())
for i in range(M):
  A,B = map(int,input().split())
  G[A].append(B)
  H[B].append(A)

for i in range(1,N+1):
  if used[i] == False:
    dfs(i)

ans = 0
for i in range(1,N+1):
  used[i] = False

I.reverse()
for i in I:
  if used[i] == True:
    continue
  cnts = 0 # 何個の頂点から構成されるグループかを示す
  dfs2(i)
  ans += cnts*(cnts-1)/2 # cnts個の頂点から構成されるグループでは、お互いに行き来できるパスの数はcntsから2個を選択するのでcntsC2 = cnts*c(nts-1)/2

print(int(ans))