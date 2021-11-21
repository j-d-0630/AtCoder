N = int(input())
S = input()
# dp = [[インクリメント用,aまで合ってる物の数,atまで合ってるの物の数,atcまで合ってる物の数,atco,atcod,atcode,atcoderまで合ってる物の数],[],[],[]]
# インクリメント用に1、atcoderで7の計8要素 × 入力最大文字数100000の配列となる
dp = [[0]*8 for _ in range(100001)]
mod = 1000000007

# Dynamic Programming(動的計画法)
dp[0][0] = 1
for i in range(N): #全ての入力文字を順番に評価
  for j in range(8):
    dp[i+1][j] += dp[i][j] # 前回までの結果をコピー
    if S[i] == "a" and j == 0: dp[i+1][j+1] += dp[i][j] # aが出現したときは、1を加える
    if S[i] == "t" and j == 1: dp[i+1][j+1] += dp[i][j] # tが出現したときは、これまでの評価でaまで合っている物の数を加える
    if S[i] == "c" and j == 2: dp[i+1][j+1] += dp[i][j] # cが出現したときは、これまでの評価でatまで合っている物の数を加える
    if S[i] == "o" and j == 3: dp[i+1][j+1] += dp[i][j]
    if S[i] == "d" and j == 4: dp[i+1][j+1] += dp[i][j]
    if S[i] == "e" and j == 5: dp[i+1][j+1] += dp[i][j]
    if S[i] == "r" and j == 6: dp[i+1][j+1] += dp[i][j] # rが出現したときは、これまでの評価でatcodeまで合っている物の数を加える
  for k in range(8): # 毎回割って余りにしておく
    dp[i+1][k] %= mod

# 最後の文字を評価しatcoderまで合っている物の数は、dp[N][7]に格納されている
print(dp[N][7])
