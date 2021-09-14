"""
AとBの最小公倍数は A*B / (AとBの最大公約数)
"""
import math

A,B = map(int,input().split())
gcd = math.gcd(A,B)
ans = A*B // gcd

if ans > 1000000000000000000:
  ans = "Large"

print(ans)