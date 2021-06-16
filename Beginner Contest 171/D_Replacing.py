from collections import Counter

N = int(input())
A = list(map(int,input().split()))
Q = int(input())

counter = Counter(A) #Counterは辞書型で出力する
sum_res = sum(A)

for _ in range(Q):
  B, C = map(int,input().split())

  sum_res -= B * counter[B]
  sum_res += C * counter[B]

  counter[C] += counter[B]
  counter[B] = 0

  print(sum_res)