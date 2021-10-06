"""
ランレングス圧縮
"""
N = int(input())
S = input()

vec = [] # ○だけしか含まれない区間、×だけしか含まれない区間
cnt = 0
for i in range(N):
  cnt += 1
  if i == N-1 or S[i] != S[i+1]: # 最後まで到達するか○×が変わったらvecに連続数を格納
    vec.append(cnt)
    cnt = 0

# ○だけor×だけの区間は解になり得ないので、その区間での(l,r)の組み合わせ数を求め、最後に全組み合わせから差し引くことで答えが求まる
ret = 0
for i in range(len(vec)):
  if vec[i] % 2 == 0:
    ret += (vec[i] // 2) * (vec[i] + 1)
  else:
    ret += (vec[i] // 2) * (vec[i] + 1) + (vec[i] + 1) // 2

# (l,r)の全組合わせの数 = 1+2+3+,,,,N
if N % 2 == 0:
  all = N // 2 * (N+1)
else:
  all = N // 2 * (N+1) + (N+1) // 2

ans = all - ret
print(ans)