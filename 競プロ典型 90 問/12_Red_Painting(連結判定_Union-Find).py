"""
連結判定はUnion-Find
Union-Find 木は、N個の点に対して、次の2種類の操作を高速に行うもの。
①リンク：x,yが指定され、xの点とyの点をつなぐ。
②連結判定：x,yが指定され、今までにつないだ線だけを辿って、xとyを行き来できるかを判定する。

■解法
・隣り合う赤マスを線でつないでいく
"""

# Union Findクラス
class UnionFind:
  def __init__(self,n):
    self.n = n
    self.parent = [-1] * n # 自身が子なら親node番号を格納。親ならその下に繋がるnode数を負で格納する。
  
  def root(self,x) -> int:
    """
    xの根を取得
    """
    if self.parent[x] < 0: # 負ということは親nodeである
      return x
    else:
      self.parent[x] = self.root(self.parent[x]) # 負になるまで探索（親nodeに辿り着くまで探索）
      return self.parent[x]
  
  def unite(self,x,y) -> int:
    """
    xとyを併合
    """
    x = self.root(x)
    y = self.root(y)

    if x == y: # 入力(A,B)の親nodeが同じということは既に連結されているのでreturnして終了
      return 0
    
    if self.parent[x] > self.parent[y]: # node[x]よりnode[y]の方がこの数が多い場合は入れ替える※parentは負の値
      x,y = y,x
    
    self.parent[x] += self.parent[y] # 下に繋がる子node数を追加していく
    self.parent[y] = x # 親node番号を格納。(併合することでyの親もxと同じになる)

    return self.parent[x]
  
  def size(self,x) -> int:
    """
    xが属する連結成分のサイズを取得
    """
    return -self.parent[self.root(x)]


# その他の関数
def query1(px,py):
  dx = [-1,0,1,0] # 移動方向
  dy = [0,1,0,-1] # 移動方向
  for i in range(4): # 上下左右の4方向全ての移動パターンにおいて赤マスが隣あっているか調べる
    sx = px + dx[i] # 移動先
    sy = py + dy[i] # 移動先
    if used[sx][sy] == False: # 白マスならスキップし次の移動パターンを調べる
      continue
    hash1 = px * W + py # hashにより座標を一意に定義する
    hash2 = sx * W + sy
    uf.unite(hash1,hash2) # 隣合う赤マスを連結
  
  used[px][py] = True # 赤マスに塗る


def query2(px,py,qx,qy):
  if used[px][py] == False or used[qx][qy] == False:
    return False
  
  hash1 = px * W + py
  hash2 = qx * W + qy
  if uf.root(hash1) == uf.root(hash2): # 親nodeが同じなら繋がっているということ
    return True
  else:
    return False


#解
# step1 入力
H,W = map(int,input().split())
Q = int(input())
used = [ [False]*2009 for _ in range(2009)]

# step2 Union Find の初期化
uf = UnionFind(H * W)

# step3 クエリ処理
for i in range(Q):
  q = list(map(int,input().split()))
  if q[0] == 1:
    px = q[1]
    py = q[2]
    px -= 1
    py -= 1
    query1(px,py)

  if q[0] == 2:
    px = q[1]
    py = q[2]
    qx = q[3]
    qy = q[4]
    px -= 1
    py -= 1
    qx -= 1
    qy -= 1
    ans = query2(px,py,qx,qy)
    if ans:
      print("Yes")
    else:
      print("No")
