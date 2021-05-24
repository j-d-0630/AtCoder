from itertools import permutations
import itertools
N,K = map(int,input().split())
T = [list(map(int,input().split())) for i in range(N)]

town = list(range(1,N+1))
ans = 0
for i in itertools.permutations(town):
  distance = 0
  if i[0] == 1:
    for j in range(N-1):
      distance += T[i[j]-1][i[j+1]-1]
    distance += T[i[N-1]-1][i[0]-1]
    if distance == K:
      ans += 1

print(ans)
