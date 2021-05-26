N = int(input())
A = list(map(int,input().split()))
A.insert(0,0) #index調整のために先頭に0を加える。（0回目の移動という意味）

P = [0]*(N+1) #i回目の動き後の現在地。つまりP[0]はスタート位置
S = [0]*(N+1) #i回目の動きの変動量
M = [0]*(N+1) #i回目の動き内の最大位置。

#P[i-1]+M[i]がそれまでのansを上回ればansを更新していく。
ans = -100000000
for i in range(1,N+1):
  M[i] = max(M[i-1],S[i-1] + A[i])
  tmp = P[i-1] + M[i]
  if tmp > ans:
    ans = tmp
  
  S[i] = S[i-1] + A[i]
  P[i] = P[i-1] + S[i] #現在地更新

print(ans)
