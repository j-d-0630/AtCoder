import math

N,M = map(int,input().split())
if M != 0:
  A = list(map(int,input().split()))
  A.sort()

  #番兵追加 → 先頭と末端に「0」と「N+1」を入れることで先頭と末端の白マスの長さを表現しやすくする
  A.insert(M,N+1)
  A.insert(0,0)

  #白マスの塊（連続数）の最小値を求める。同時に白マスの塊ごとのリストを作成
  min_w = N
  width_l = []
  for i in range(M+1):
    width = A[i+1] - A[i] - 1
    if width > 0:
      width_l.append(width)
      if width < min_w:
        min_w = width

  #答えを求める
  ans = 0
  if len(width_l) != 0:
    for i in range(len(width_l)):
      ans += math.ceil(width_l[i] / min_w)

else:
  ans = 1

print(ans)