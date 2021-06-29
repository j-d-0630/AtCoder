N,K = map(int,input().split())
A = [0] + list(map(int,input().split())) #町番号とindexを揃えるため,先頭に0を加えておく

order = [-1] * (N+1) #町iに到達したときの総移動回数

seen = [] # 訪れた町のリスト
pos = 1 # 現在いる町。1からスタート

while order[pos] == -1: # 同じ町に再び訪れるまで繰り返す
  order[pos] = len(seen)
  seen.append(pos)
  pos = A[pos]

period = len(seen) - order[pos] # 循環の周期
m = order[pos] # 循環し始めるタイミング

if K < m: # 循環前に終わる場合
  print(seen[K]) # K回目の移動で訪れる町
else: # 循環する場合
  print(seen[m + (K - m) % period]) # 循環開始までの移動回数 + (循環開始後の移動回数)%循環周期