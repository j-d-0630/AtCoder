import math
L = int(input())
# N-1個の切れ目から11個を選択するパターン数を計算する
ans = math.factorial(L-1) // (math.factorial(L-1-11) * math.factorial(11))
print(ans)
