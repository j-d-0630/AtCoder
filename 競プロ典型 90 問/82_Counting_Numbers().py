"""

"""
L,R = map(int,input().split())
mod = 1000000007

# 1+2+3+,,,,,Nの計算
def f(x):
  if x % 2 == 0:
    return ((x+1)*x//2) % mod
  else:
    return ((x+1)*(x//2) + (x+1)//2) % mod

ans = 0
for i in range(1,20): # 1桁～19桁の数まで計算する
  l = max(L,10**(i-1)) # 1桁の時はLか1か
  r = min(R,10**i-1) # 1桁の時はRか9か
  if l > r:
    continue
  val = (f(r) - f(l-1)) % mod # l～rまでの数字が何個あるか
  ans += val * i

print(ans%mod)