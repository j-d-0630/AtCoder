"""
累積和のアルゴリズムを多次元に拡張したものをいもす法と呼ぶ。
"""
N = int(input())
S = [list(map(int,input().split())) for _ in range(N)]
H = W = 1000

# 座標
dat = [[0]*(W+1) for _ in range(H+1)]

# 各長方形の四隅の位置情報を記載
for lx, ly, rx, ry in S:
  dat[ly][lx] += 1
  dat[ry][lx] -= 1
  dat[ry][rx] += 1
  dat[ly][rx] -= 1

# 二次元累積和をとることで、datの各座標の値が重なっている紙の枚数になる
def np_x_zeta(x,initial=None):
  if isinstance(x[0], list): # 型判定
    for i in range(len(x)):
      np_x_zeta(x[i], initial=initial)
    if initial is not None:
      x.insert(0, [initial]*len(x[0]))
    for j in range(len(x[0])): # y方向に累積和を取る
      for i in range(1, len(x)):
        x[i][j] += x[i-1][j]
  else: # x方向に累積和をとる
    if initial is not None:
      x.insert(0, initial)
    for i in range(1, len(x)):
      x[i] += x[i-1]

np_x_zeta(dat)

ans = [0] * (N+1)
for x in range(W+1):
  for y in range(H+1):
    ans[dat[y][x]] += 1

for n in range(1,N+1):
  print(ans[n])