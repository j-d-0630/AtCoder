n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

res = 0
for i in range(1,1001):
  ok = True
  for j in range(n):
    if i < a[j] or i > b[j] : ok = False
  
  if ok == True : res += 1

print(res)