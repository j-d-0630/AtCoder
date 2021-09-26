"""

"""
N,K = map(int,input().split())

N = str(N)

# 8進数の文字列で入力
def cal10(n:str) -> int:
  tmp10 = 0
  for i in range(len(n)):
    tmp10 += int(n[len(n)-1-i]) * 8**i
  return tmp10

# 10進数の整数で入力
def cal9(n:int) -> str:
  tmp9 = ""
  for i in range(20):
    tmp9 += str(n // 9**(19-i))
    n = n % 9**(19-i)
  
  tmp9 = list(tmp9)
  for i in range(len(tmp9)):
    if tmp9[i] == "8":
      tmp9[i] = "5"
  
  tmp9_2 = ""
  for s in tmp9:
    tmp9_2 += s

  return tmp9_2

for _ in range(K):
  N = cal10(N)
  N = cal9(N)

print(int(N))