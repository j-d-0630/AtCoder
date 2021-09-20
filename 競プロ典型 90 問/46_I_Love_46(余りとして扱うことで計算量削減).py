"""
ある数値の和がある値で割り切れるかどうかの判定は各数値をある値で割った余りの和が0になればよい
よって各数値をある値で割っておき数値の種類を減らすことで計算量を減らす
"""
from collections import Counter

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

# 1だろうが47だろうが、46で割った余りが同じなら同じものとして扱える
for i in range(N):
  A[i] = A[i]%46
  B[i] = B[i]%46
  C[i] = C[i]%46

# 同じ余りのものの数を数える。46の余りなので最大でも46種 → 全探索できるように母数を減らす
cnt_A = Counter(A)
cnt_B = Counter(B)
cnt_C = Counter(C)

# 最大46**3組なので全探索でいく
ans = 0
for a in cnt_A:
  for b in cnt_B:
    for c in cnt_C:
      if (a + b + c)%46 == 0:
        # (a,b,c)となる組み合わせはaの数*bの数*cの数
        ans += cnt_A[a]*cnt_B[b]*cnt_C[c]

print(ans)