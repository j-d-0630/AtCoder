"""
尺取り法
"""
S = list(input())
K = int(input())

ans = 0
cr = 0 # 現在探索しているindex
cnt = 0 # "."に遭遇した回数

for i in range(len(S)):
  while(cr <= len(S)-1):
    if S[cr] == "." and cnt == K:
      break
    if S[cr] == ".":
      cnt += 1
    cr += 1
  ans = max(ans,cr-i)
  if S[i] == ".":
    cnt -= 1

print(ans)