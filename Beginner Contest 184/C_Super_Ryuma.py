r1,c1 = map(int,input().split())
r2,c2 = map(int,input().split())

#開始点の切片
#y=x+?の切片
intercept_1 = c1 - r1
#y=-x+?の切片
intercept_2 = c1 + r1

#目標点の切片
#y=x+?の切片
intercept_3 = c2 - r2
#y=-x+?の切片
intercept_4 = c2 + r2

#開始点と目標点が同じ場合
if r1 == r2 and c1 == c2:
  ans = 0
#3マス以下の移動で到達する場合
elif (abs(r2-r1) + abs(c2-c1)) <= 3:
  ans = 1
#1回の斜め直進移動で到達する場合。y=xで移動する場合とy=-xで異動する場合の2パターン
elif c2 - r2 - intercept_1 == 0 or c2 + r2 - intercept_2 == 0:
  ans = 1
#2回の斜め直進移動で到達する場合
elif ((intercept_1 + intercept_4)%2  == 0 and (-intercept_1 + intercept_4)%2 == 0) or ((intercept_2 + intercept_3)%2  == 0 and (-intercept_2 + intercept_3)%2 == 0):
  ans = 2
#1回の斜め直進移動と3マス以下の移動で到達する場合
elif (abs((intercept_1 + intercept_4)/2 - c2) + abs((-intercept_1 + intercept_4)/2 - r2)) <= 3 or (abs((intercept_2 + intercept_3)/2 - c2) + abs((intercept_2 - intercept_3)/2 - r2)) <= 3:
  ans = 2
#2回の3マス以下の移動で到達する場合
elif (abs(r2-r1) + abs(c2-c1)) <= 6:
  ans = 2
#その他
else:
  ans = 3

print(ans)


#以下は解説の回答方法
# r1, c1 = map(int, input().split())
# r2, c2 = map(int, input().split())
# r = r2 - r1
# c = c2 - c1
#開始点と目標点が同じ場合
# if (r, c) == (0, 0):
#     ans = 0
#1回の斜め直進移動で到達する場合。y=xで移動する場合とy=-xで異動する場合の2パターン
# elif r == c or r == -c: 
#     ans = 1
#3マス以下の移動で到達する場合
# elif abs(r) + abs(c) <= 3:
#     ans = 1
#2回の斜め直進移動で到達する場合(rとcの偶奇が揃っている場合にこの条件にはまる。<理由>斜め直進移動ではr、cの数値は＋1か－1となるので、rとcの偶奇は一致する。)
# elif (r ^ c ^ 1) & 1:
#     ans = 2
#2回の3マス以下の移動で到達する場合
# elif abs(r) + abs(c) <= 6:
#     ans = 2
#1回の斜め直進移動と3マス以下の移動で到達する場合
# elif abs(r + c) <= 3 or abs(r - c) <= 3:
#     ans = 2
# else:
#     ans = 3
# print(ans)
