  
def solve(mid,N,K,A_list):
  count = 0
  pre = 0
  for i in range(0,N):
    if (A_list[i] - pre >= mid) and (L - A_list[i] >= mid):
      count += 1
      pre = A_list[i]
  
  if count >= K:
    return True
  else:
    return False


N,L = map(int,input().split())
K = int(input())
A_list = list(map(int,input().split()))

left = 0
right = L

while right - left > 1:
  mid = int(left + (right - left)/2)
  if solve(mid, N, K, A_list) == False:
    right = mid
  else:
    left = mid

print(left)
