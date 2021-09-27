"""
繰り返し2乗法
"""
N,K = map(int,input().split())
mod = 1000000007

def binpower(a:int,b:int) -> int:
  ans = 1
  while b != 0:
    if b % 2 == 1:
      ans = ans * a % mod
    a = a * a % mod
    b //= 2
  return ans

if K == 1:
  if N == 1:
    ans = 1
  else:
    ans = 0
elif N == 1:
  ans = K % mod
elif N == 2:
  ans = K*(K-1) % mod
else:
  ans = K * (K-1) % mod * binpower(K-2,N-2) % mod

print(ans)