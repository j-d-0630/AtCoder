import string

N = int(input())
A = list(string.ascii_lowercase)

ans = ""
while N:
  N -= 1
  ans += A[N%26]
  N //= 26

print(ans[::-1])
