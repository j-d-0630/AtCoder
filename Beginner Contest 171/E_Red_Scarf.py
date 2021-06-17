N = int(input())
A = list(map(int,input().split()))

s = A[0]
'''
a XOR a = 0 、a XOR a XOR a = a　であることを利用する
'''
for num in A[1:]:
  s ^= num

ans = [0] * N
for i, num in enumerate(A):
  ans[i] = s ^ num

print(*ans)
