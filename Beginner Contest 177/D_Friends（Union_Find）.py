class UnionFind():
  def __init__(self,n):
    self.parents = [-1] * n #自身が子なら親node番号を格納。親ならその下に繋がるnode数を格納する
  
  def find(self,x): #自身が親か子かを判断する
    if self.parents[x] < 0: #負ということは親nodeである
      return x
    else:
      self.parents[x] = self.find(self.parents[x]) #負になるまで探索（親nodeに辿り着くまで探索）
      return self.parents[x]
  
  def union(self,x,y):
    x = self.find(x)
    y = self.find(y)

    if x == y: #入力(A,B)の親nodeが同じだと連結する子の数は増えないので、子node数を追加することなくreturnして終了
      return
    
    if self.parents[x] > self.parents[y]: #node[x]よりnode[y]の方が子の数が多い場合は入れ替える
      x,y = y,x
    
    self.parents[x] += self.parents[y] #下に繋がる子nodeの数を追加していく
    self.parents[y] = x #親node番号を格納


N,M = map(int,input().split())
info = [ tuple(map(int,input().split())) for s in range(M)]

uf = UnionFind(N)
for a, b in info:
  a -= 1
  b -= 1
  uf.union(a,b)

ans = min(uf.parents) #最も連結する子nodeの数が多いものが解
print(-ans)
