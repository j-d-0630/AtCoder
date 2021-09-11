#右90°回転
def rot(S):
  return list(zip(*S[::-1]))

#左上の'#'の位置を探す
def find_left_top(S):
  for i in range(N):
    for j in range(N):
      if S[i][j] == '#':
        return i,j

#一致しているか判定
def is_same(S,T):
  Si,Sj = find_left_top(S)
  Ti,Tj = find_left_top(T)
  offset_i = Ti-Si
  offset_j = Tj-Sj
  for i in range(N):
    for j in range(N):
      ii = i+offset_i
      jj = j+offset_j
      if 0 <= ii < N and 0 <= jj < N: # オフセットさせた場合に'#'が枠内に入っていればOK
        if S[i][j] != T[ii][jj]: return False # SとオフセットさせたTが一致しているか比較
      else: # オフセットさせた場合に'#'が枠外に出てしまう場合はNG
        if S[i][j] == '#': return False
  return True

N = int(input())
S = [input() for _ in range(N)]
T = [input() for _ in range(N)]

cntS = sum(1 for i in range(N) for j in range(N) if S[i][j]=='#')
cntT = sum(1 for i in range(N) for j in range(N) if T[i][j]=='#')

if cntS != cntT: # そもそも'#'の数が異なっていたらNG
  print("No")
  exit()

for _ in range(4): # 最大4回回転
  if is_same(S,T):
    print("Yes")
    exit()
  S = rot(S) # 回転

print("No")
