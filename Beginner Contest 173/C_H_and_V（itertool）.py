import itertools

h,w,k = map(int,input().split())
A = [list(input()) for _ in range(h)]

ans = 0

#全ての塗りつぶし方。塗りつぶすときを"0"、塗らないときを"1"で表現
for row_bit in itertools.product(range(2),repeat=h):
  for col_bit in itertools.product(range(2),repeat=w):
    cnt = 0 #黒マスの数
    #マスを一つずつ調べていく
    for row in range(h):
      for col in range(w):
        #元々黒色かつ塗りつぶされない場合に当てはまればcntをインクリメントする
        if A[row][col] == "#" and (row_bit[row] and col_bit[col]):
          cnt += 1
    if cnt == k:
      ans += 1

print(ans)
