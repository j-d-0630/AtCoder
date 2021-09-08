from collections import defaultdict

N = int(input())
d = defaultdict(int)

for i in range(N):
  tmp = input()
  if d[tmp] == 0: # 未知ならば
    d[tmp] += i+1

for i in d.values():
  print(i)