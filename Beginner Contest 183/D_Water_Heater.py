N,W = map(int,input().split())
water_1 = [0]*(2*10**5+1) #各時間のお湯の出入り量
water_2 = [0]*(2*10**5+1) #各時間のお湯の使用量

for i in range(N):
  S,T,P = map(int,input().split())
  water_1[S] += P
  water_1[T] -= P

ans = "Yes"
for i in range(2*10**5):
  water_2[i+1] += (water_2[i] + water_1[i]) #water_1が出入りし、water_2の値を更新していく。water_2がWを超えればNoを返す
  if water_2[i] > W:
    ans = "No"
    break

print(ans)