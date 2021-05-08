N,K = map(int,input().split())

for i in range(K):
  if N%200 == 0:
    N = N/200

  else:
    N = N*1000 + 200

print(int(N))