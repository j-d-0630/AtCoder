N = int(input())
A = list(map(int,input().split()))

A.sort(reverse=True) #大きい順にソート
B = [] #既に到着した人
cnt = 0
for a in A:
  if len(B) != 0:
    j = len(B) // 2
    cnt += B[j]
  
  B.append(a)

print(cnt)