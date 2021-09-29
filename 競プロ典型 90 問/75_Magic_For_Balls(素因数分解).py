"""
素因数分解
2,3,4,5,6,,,,,√Nより小さい整数で割り続ける
"""
import math

# 素因数分解
def prime_factors(n:int):
  rem = n
  p = []
  tgt = math.floor(math.sqrt(rem))
  for i in range(2,tgt+1):
    while rem % i == 0:
      rem //= i
      p.append(i)
  if rem != 1:
    p.append(rem)
  return p


N = int(input())
vec = prime_factors(N)

for i in range(21):
  if 1 << i >= len(vec): # 2のi乗がvecの要素数を上回ったときが答え
    ans = i
    break

print(ans)