"""

"""
N,K = map(int,input().split())
vec = [] # 1分間でできる得点方法のリスト

for _ in range(N):
  A,B = map(int,input().split())
  vec.append(B) # N問目に関してまず1分間で部分点を得られる
  vec.append(A-B) # 更に1分かけると部分点とフル回答の差分の特定が得られる

# どの問題から解くと得点効率が良いかはvecを降順にソートすれば分かる

ans = 0
vec.sort(reverse=True) # sortして最も得点効率の高いものから順に並べる
for i in range(K): #Ｋ分間の間に得点効率の高い方法を実施していきKに到達したら終了
  ans += vec[i]

print(ans)