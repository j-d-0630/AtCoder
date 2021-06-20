#ある要素と要素が連結かどうかを管理するには、UnionFindというデータ構造を使うのが楽
from typing import List

class UnionFind:
  def __init__(self,n):
    self.n = n
    self.parent = [-1] * n #自身が子なら親node番号を格納。親ならその下に繋がるnode数を格納する
  
  def root(self,x) -> int:
    """
    xの根を取得
    """
    if self.parent[x] < 0: #負ということは親nodeである
      return x
    else:
      self.parent[x] = self.root(self.parent[x]) #負になるまで探索（親nodeに辿り着くまで探索）
      return self.parent[x]
  
  def unite(self,x,y) -> int:
    """
    xとyを併合
    """
    x = self.root(x)
    y = self.root(y)

    if x == y: #入力(A,B)の親nodeが同じということは、既に連結されているのでreturnして終了
      return 0
    
    if self.parent[x] > self.parent[y]: #node[x]よりnode[y]の方が子の数が多い場合は入れ替える
      x,y = y,x
    
    self.parent[x] += self.parent[y] #下に繋がる子nodeの数を追加していく
    self.parent[y] = x #親node番号を格納

    return self.parent[x]
  
  def size(self,x) -> int:
    """
    xが属する連結成分のサイズを取得
    """
    return -self.parent[self.root(x)]
  
  def all_size(self) -> List[int]:
    """
    全連結成分のサイズのリストを取得
    """
    sizes = []

    for i in range(self.n):
      size = self.parent[i]
      if size < 0:
        sizes.append(-size)
    return sizes
  
  def groups(self) -> List[List[int]]:
    """
    全連結成分のサイズの内容のリストを取得
    """
    groups = dict()

    for i in range(self.n):
      p = self.root(i)
      if not groups.get(p):
        groups[p] = []
      groups[p].append(i)
    
    return list(groups.values())


def main():
  N = int(input())
  A = list(map(int,input().split()))

  def solve():
    Const = 2 * 10 ** 5 + 5
    uf = UnionFind(Const)
    if N % 2 == 0:
      first = A[:N // 2]
      second = A[N // 2:][::-1]
    else:
      first = A[:N // 2]
      second = A[N // 2 + 1:][::-1]
    
    for x, y in zip(first,second):
      uf.unite(x,y)
    
    ans = 0
    for x in uf.all_size():
      ans += x - 1
    
    return ans
  
  rslt = solve()
  print(rslt)

if __name__ == "__main__":
  main()
