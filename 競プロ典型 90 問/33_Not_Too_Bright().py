"""

"""
import math

H,W = map(int,input().split())

if H == 1 or W == 1:
  ans = H * W
else:
  ans = math.ceil(H/2) * math.ceil(W/2)

print(ans)