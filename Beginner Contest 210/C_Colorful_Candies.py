N,K = map(int,input().split())
C = list(map(int,input().split()))

color = {} # 辞書型
for i in range(N):
  color.setdefault(C[i],0)

tmp = 0
for i in range(K):
  if color[C[i]] == 0: # 未出現の場合はキャンディの色数を増やす
    tmp += 1
  color[C[i]] += 1

ans = tmp

for i in range(N-K):
  if color[C[i]] == 1: # 1回しか出現していないものは無くなるのでキャンディの色数を減らす
    tmp -= 1
  color[C[i]] -= 1

  if color[C[i+K]] == 0: # 未出現の場合はキャンディの色数を増やす
    tmp += 1
  color[C[i+K]] += 1
  ans = max(ans, tmp)

print(ans)
