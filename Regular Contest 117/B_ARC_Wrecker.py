#input
N = int(input())
A = list(map(int,input().split()))
A.sort()

#calculate Q
Q = [0 for i in range(N)]
Q[0] = A[0]
for i in range(1,N):
  Q[i] = A[i] - A[i-1]

#calculate the answer
Answer = 1
for i in range(N):
  Answer *= (Q[i] + 1)
  Answer %= (10**9 + 7)

#output
print(Answer)
