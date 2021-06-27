"""
10進数→26進数（アルファベットで表記）に変換
・26で割った余りが一文字目となる → 26で割った商を再評価 → 26で割った余りが次の文字
　商が0になるまで以降繰り返し
・最後に文字列を反転　→　ans[::-1]
・文字列は ans= "", ans += "a" , ans += "b"   とすることでans = "ab" と表記できる
"""

import string

N = int(input())
A = list(string.ascii_lowercase)

ans = ""
while N:
  N -= 1
  ans += A[N%26]
  N //= 26

print(ans[::-1])