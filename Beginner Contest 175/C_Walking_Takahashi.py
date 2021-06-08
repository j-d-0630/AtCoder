x, k, d = map(int,input().split())
cur = abs(x)
rem = k # 残りの移動回数

cnt = min(cur // d, k) # 0に向かって移動する回数
cur -= d * cnt
rem -= cnt

if rem > 0:
  if rem % 2 == 1:
    cur = cur - d

ans = abs(cur)

print(ans)
