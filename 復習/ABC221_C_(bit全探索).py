N = input()
N = sorted(N,reverse=True) # 降順ソート

ans = 0
# bit全探索
for i in range(1 << len(N)): # N桁なので、lに振り分けるかrに振り分けるかの組み合わせは2**N通り
  l = 0
  r = 0
  for j in range(len(N)): # iの各bitが0か1かを調べていく
    if i & (1 << j): # iのjbitが1ならlへ振り分ける
      l = l * 10 + int(N[j])
    else: # iのjbitが1ならrへ振り分ける
      r = r * 10 + int(N[j])
  ans = max(ans,l*r)

print(ans)