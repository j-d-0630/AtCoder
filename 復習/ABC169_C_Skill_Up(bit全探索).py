"""
・bit全探索
・list同士の足し算はmap(sum,zip(list_A,list_B))
"""

N,M,X = map(int,input().split())
Book = [list(map(int,input().split())) for _ in range(N)]

price = []
#bit全探索
for i in range(2**N): # 買う買わないの全組み合わせ。2進数表現で考えれば、1 or 0 で状態を表現できる。
  skill = [0]*(M+1) # 初期化。値段もリストに含めてしまうから要素数はM+1
  for j in range(N): # N冊分を1個ずつ評価
    if ((i>>j) & 1): # 0~N bit ずらしていくことで、各bitが「1」なのか「0」なのかを調べていく
      skill = list(map(sum,zip(skill,Book[j])))
  if min(skill[1:]) >= X:
    price.append(skill[0])

if len(price) != 0:
  ans = min(price)
else:
  ans = -1

print(ans)
