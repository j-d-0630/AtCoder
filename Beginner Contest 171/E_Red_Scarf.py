from typing import List


N = int(input())
A = list(map(int,input().split()))

s = A[0]
for num in A[1:]:
  s ^= num

ans = [0] * N
for i, num in enumerate(A):
  ans[i] = s ^ num

print(*ans)