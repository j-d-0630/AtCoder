"""
・素数は互いに独立であるため、for文で順番に全て試して約数を探していけば良い
　2で何回割れるか　→　3で何回割れるか　→　5で何回割れるか　・・・
　これで2*2*2・・・3*3*・・・5*5*・・・のように素因数分解できる
・分解した因数はlistに格納後Counterで変換すると扱いやすい
"""

from collections import Counter

N = int(input())

table = [] # 素因数分解の結果を格納する
for i in range(2, int(N ** 0.5) + 1): # √Nを超えるとNでしか割りきなくなり解は1となるので、√Nまでしか探索しなくて良い
  while N % i == 0:
    table.append(i)
    N //= i

if N > 1: # 割り切れなくなった最後の商をtableに加える
  table.append(N)

C = Counter(table) # Cは辞書型

ans = 0
for i in C.values(): # 各素数の構成数を取り出す
  nx = 1 # ●●乗を意味する。まずは1乗からスタート
  while i >= nx:
    i -= nx # nx乗=素数をnx個分消費したのでiから差し引く
    ans += 1
    nx += 1 # 1乗、2乗、3乗・・・と評価していくためにインクリメントする

print(ans)
