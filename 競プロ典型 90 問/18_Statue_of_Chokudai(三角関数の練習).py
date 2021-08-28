"""
(0,0)と(x,y)の角度はatan2(y,x)で求まる
"""
import math

T = int(input())
L,X,Y = map(int,input().split())
Q = int(input())
E = [int(input()) for _ in range(Q)]

# 時刻Eの時の観覧車の位置の座標
def pre_loc(e):
  y = L / 2 * math.cos(math.radians(-90 - 360/T * e))
  z = L / 2 * math.sin(math.radians(-90 - 360/T * e)) + L / 2
  return [0,y,z]

# (x,y,z)の位置から像に対する俯角を算出
def cal(x,y,z):
  zo_loc = [X,Y,0]
  pre_loc = [x,y,z]
  tmp = math.sqrt((y-Y)**2 + (x-X)**2) # x面,y面,z面の3次元 → xy面,z面の2次元へ変換しatan2が計算できるようにする
  rad = math.atan2(z,tmp)
  ans = math.degrees(rad) # atan2()は返り値がradianのためdegreeへ変換
  return ans

for e in E:
  x,y,z = pre_loc(e)
  ans = cal(x,y,z)
  print(ans)