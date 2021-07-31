"""
優先度付きque(Priority queue)
・最小値（最大値）を O(logN)で取り出す
・要素を O(logN)で挿入する
"""
import heapq

q = int(input())

box = []
heapq.heapify(box) # リストを優先度付きキューに変換

sum = 0
for i in range(q):
  Q = list(map(int,input().split()))
  if Q[0] == 1:
    heapq.heappush(box,Q[1] - sum) # 優先度付きキューに要素を挿入
  elif Q[0] == 2:
    sum += Q[1]
  else:
    tmp = heapq.heappop(box) # 優先度付きキューから最小値を取り出す
    print(tmp + sum)
