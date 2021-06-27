"""
数え上げ問題におけるTLE対策
・前計算
・包除原理
"""
from sys import stdin
input = stdin.readline

H,W = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]

# 前計算
Row = [0]*2000
Column = [0]*2000
for i in range(H):
  for j in range(W):
    Row[i] += A[i][j] # i行目の値の和
    Column[j] += A[i][j] # j列目の値の和

# 答えの計算
ans = [[0] * W for _ in range(H)]
for i in range(H):
  for j in range(W):
    ans[i][j] += Row[i] + Column[j] - A[i][j]

# 出力
for i in range(H):
  print(*ans[i])