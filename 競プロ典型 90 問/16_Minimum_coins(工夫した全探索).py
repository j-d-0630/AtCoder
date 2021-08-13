"""
python3.8ではTLE
pypy3ではAC
"""
N = int(input())
A,B,C = map(int,input().split())

ans = 9999
for i in range(10000):
  for j in range(10000-i):
    V = N - i*A - j*B
    R = i + j + V/C
    if V%C != 0 or V < 0 or R > 9999:
      continue
    ans = min(ans,R)

print(int(ans))