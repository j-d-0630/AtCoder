from sys import stdin
input = stdin.readline

H,W,N = map(int,input().split())
X,Y = [],[]

for i in range(N):
  x,y = map(int,input().split())
  X.append(x)
  Y.append(y)

Xdict = {x:i+1 for i,x in enumerate(sorted(list(set(X))))} # iと紐づけて、Xは何番目に大きい数字かを割り当てていく
Ydict = {y:i+1 for i,y in enumerate(sorted(list(set(Y))))} # iと紐づけて、Yは何番目に大きい数字かを割り当てていく

for i in range(N):
  print(Xdict[X[i]],Ydict[Y[i]]) # X[i]、Y[i]は何番目に大きい数字かを呼び出す
