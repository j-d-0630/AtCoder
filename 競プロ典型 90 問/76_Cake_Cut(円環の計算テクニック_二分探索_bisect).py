"""
円環のままだと難しいので、二倍にした列とみなして考える
"""
import bisect

N = int(input())
A = list(map(int,input().split()))
B = [0] * (2* N + 1)

for i in range(N):
  B[i+1] = A[i] + B[i]

for i in range(N):
  B[i+N+1] = A[i] + B[i+N]

if B[N] % 10 != 0: # 1/10したものが整数でなければNG
  print("No")
  exit()

# B_Right - B_Left = L/10となる条件を探す
#B_Leftをループして変えていき全て評価。B_Leftを固定した中でB_Rightは二分探索で探す
for i in range(N):
  goal = B[i] + B[N] / 10 # goal = B_Right
  posl = bisect.bisect_left(B,goal) # B_RightはBのどの位置に入るか
  if B[posl] == goal and posl - i <= N: # B_RightがBの中に存在していてかつケーキのホール一周分内の範囲に収まっていればOK
    print("Yes")
    exit()

print("No")