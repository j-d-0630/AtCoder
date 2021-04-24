N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

tmp0 = []
for i in range(N):
  tmp = []
  for j in range(B[i]-A[i]+1):
    tmp.append(A[i]+j)
  tmp0.append(tmp)


tmp_min_l = []
for i in range(N):
  tmp = min(tmp0[i])
  tmp_min_l.append(tmp)
tmp_min_v = max(tmp_min_l) 

tmp_max_l = []
for i in range(N):
  tmp = max(tmp0[i])
  tmp_max_l.append(tmp)
tmp_max_v = min(tmp_max_l)

ans = tmp_max_v - tmp_min_v + 1
if ans < 0:
  ans = 0
print(ans)