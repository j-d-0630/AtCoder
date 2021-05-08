N = int(input())
A_ls = list(map(int,input().split()))

B_ls = [0]*200 #200で割ったときの余り(0~199)がそれぞれ何個ずつ存在するかを示すリストを作成していく

for i in range(N):
  tmp = int(A_ls[i]%200)
  B_ls[tmp] += 1

rslt = 0
for i in range(200): #余りの値の範囲である0~199までを調べる
  rslt += B_ls[i]*(B_ls[i]-1)/2

print(int(rslt))