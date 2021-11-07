N = int(input())
G = [[] for _ in range(N)]
T = [0]*N

for i in range(N):
  T[i],_,*A = map(int,input().split())
  G[i] = list(map(lambda x:x-1,A))

st = []
ans = T[N-1]
st.append(N-1)
while st:
  v = st.pop()
  for u in G[v]:
    if T[u] != -1:
      ans += T[u]
      T[u] = -1
      st.append(u)

print(ans)