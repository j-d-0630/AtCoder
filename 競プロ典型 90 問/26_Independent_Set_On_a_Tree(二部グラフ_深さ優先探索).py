"""
二部グラフの性質を使う
・木は必ず二部グラフであり2彩色（直接結ばれた頂点を互いに異なる色になるように塗る）することが可能。
  →N個の頂点を2彩色で2つのグループに分けたとき、多い方の色は1/2N個以上となるので、多い方から1/2個出力すれば解となる
・2彩色は深さ優先探索で実装できる
"""
#3個実行エラーが直せない

#input
N = int(input())
G = [ [] for _ in range(N+1) ] #頂点の連結関係を示すグラフ
col = [0]*(N+1) #各頂点の色

for _ in range(N-1):
  A,B = map(int,input().split())
  G[A].append(B)
  G[B].append(A)


#2彩色する深さ優先探索を定義
def dfs(pos:int, cur:int): # pos:頂点の番号, cur:塗りたい色。1か2に塗り分けていく
  col[pos] = cur
  for i in G[pos]:
    if col[i] >= 1: #既に塗り終わっているものはスキップし次へ
      continue
    dfs(i, 3-cur) #curが1なら3-cur=2となり2に塗れる、cur=2なら3-cur=1となり1に塗れる。dfsで1,2交互に塗っていく


#グラフを2彩色
dfs(1,1) #まずは頂点1を1に塗ることでスタートし、dfsで1,2,1,2と交互に塗っていく

# Get Answer
G1 = []
G2 = []
for i in range(1,N+1):
  if col[i] == 1:
    G1.append(i)
  else:
    G2.append(i)

if len(G1) >= len(G2):
  for i in range(N//2):
    print(G1[i],end=" ")
else:
  for i in range(N//2):
    print(G2[i],end=" ")