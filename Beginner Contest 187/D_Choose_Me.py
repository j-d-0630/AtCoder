N = int(input())

max_aoki = 0
sum_list = []
for i in range(N):
  # 各町の青木派、高橋派を読み込む
  A,B = map(int,input().split())
  max_aoki += A #青木派が獲得できる最大票数（高橋が演説にいかなかった場合）
  sum_list.append(A+B+A) #各町に演説に行った場合の票の動き（青木と高橋の票が縮まる数）

sum_list.sort(reverse=True)

ans = 0
for i in range(len(sum_list)):
  max_aoki -= sum_list[i]
  if max_aoki < 0:
    ans = i+1
    break

print(ans)
