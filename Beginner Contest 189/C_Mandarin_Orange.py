N = int(input())
A = list(map(int,input().split()))
 
B = sorted(set(A))

def calc(l,r,x):
  rslt = (r-l+1)*x
  return rslt

ans = 0
for i in range(len(B)):
  x = B[i]

  l = 0
  r = N-1

  flg = 0
  for j in range(N):
    if A[j] >= x and not(flg):
      l = j
      flg = 1
    elif A[j] < x and flg:
      r = j-1
      tmp = (r-l+1)*x
      if ans < tmp:
        ans = tmp
      flg = 0
  
  if flg:
    r = j
    tmp = (r-l+1)*x
    if ans < tmp:
        ans = tmp

print(ans)
