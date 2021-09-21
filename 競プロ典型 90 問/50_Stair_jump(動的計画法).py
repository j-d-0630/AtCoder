"""
漸化式を立てて動的計画法をする
・dp[i] = 1 (i = 0) 漸化式の初期値。0段目に到達する方法は1通り
・dp[i] = dp[i-1] (1 <= i < L) iがLより小さい領域ではiへはdp[i-1]から1段で到達するしかない
・dp[i] = dp[i-1] + dp[i-L] (i >= L) iがLより大きい領域ではiへはdp[i-1]から1段で到達するかdp[i-L]かL段で到達するか
"""
N,L = map(int,input().split())
mod = 1000000007

dp = [0] * (N+1)
dp[0] = 1

for i in range(1,N+1):
  if i < L:
    dp[i] += dp[i-1] % mod
  else:
    dp[i] += (dp[i-1] + dp[i-L]) % mod

print(dp[N] % mod)