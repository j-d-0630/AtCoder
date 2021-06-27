"""
・a XOR a = 0 、a XOR a XOR a = a　であることを利用する
・XORの演算子は ^
"""

N = int(input())
A = list(map(int,input().split()))

"""
各値の関係は以下
ans[1] ^ ans[2] ^ ans[3] = A[0]
ans[0] ^ ans[2] ^ ans[3] = A[1]
ans[0] ^ ans[1] ^ ans[3] = A[2]
ans[0] ^ ans[1] ^ ans[2] = A[3]
これら全てでXORを計算すると、a XOR a = 0 、a XOR a XOR a = a　であることを利用すると以下のように変換できる
ans[0] ^ ans[1] ^ ans[2] ^ ans[3] = A[0] ^ A[1] ^ A[2] ^ A[3]
"""

#上記の右辺を計算
s = A[0]
for num in A[1:]:
  s ^= num

"""
ans[0] ^ ans[1] ^ ans[2] ^ ans[3] = sと置き、
ans[0] = s ^ ans[1] ^ ans[2] ^ ans[3] となる
"""
ans = [0] * N
for i, num in enumerate(A):
  ans[i] = s ^ num