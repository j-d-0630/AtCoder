"""
周期性を見つけ計算量を減らす
"""
# 手順1 各桁の和の計算
def digit_sum(x:int):
  ans = 0
  while x > 0:
    ans += x % 10
    x //= 10
  return ans

N,K = map(int,input().split())
mod = 100000

# 手順2 zの算出
nxt = [0] * mod # zを全ての取り得るxから計算して配列で保存
for i in range(mod):
  nxt[i] = (i + digit_sum(i)) % mod

time_stamp = [-1] * mod
pos = N
cnt = 0 # ボタンプッシュ回数
while time_stamp[pos] == -1: # 計算したことのある数値に再度遭遇するまで繰り返す
  time_stamp[pos] = cnt
  pos = nxt[pos] # posをzに変更
  cnt += 1 # ボタンを押す
  #time_stamp[pos]が-1以外であるものと遭遇する=1周期終了

cycle = cnt - time_stamp[pos] # 周期（何回ボタンプッシュで1周期が形成されているか）

if K >= time_stamp[pos]: # ループに入っている場合
  K = (K - time_stamp[pos]) % cycle + time_stamp[pos] # 周期内で何step目にいるか

answer = -1
for i in range(mod):
  if time_stamp[i] == K:
    answer = i

print(answer)