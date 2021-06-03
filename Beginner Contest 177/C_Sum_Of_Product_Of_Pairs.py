N = int(input())
A = list(map(int,input().split()))

mod = 1000000007
ans = 0
tmp = 0
for i in range(N-1):
  tmp += A[i]
  tmp2 = A[i+1]
  ans += (tmp*tmp2)%mod

print(ans%mod)
