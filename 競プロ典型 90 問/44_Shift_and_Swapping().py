"""

"""
N,Q = map(int,input().split())
A = list(map(int,input().split()))

shift = 0
for _ in range(Q):
  T,x,y = map(int,input().split())
  if T == 1:
    A[x-1-shift],A[y-1-shift] = A[y-1-shift],A[x-1-shift]
  elif T == 2:
    shift = shift % N + 1 # 普通に+1してしまうとshiftが大きな数になり誤差が出るので、shift%N + 1としshiftがN以下になるようにする
  else:
    print(A[x-1-shift])