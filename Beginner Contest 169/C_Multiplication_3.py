A,B = input().split()
 
a = int(A)
b = int(B.replace(".","")) #「.」を削除することで、例えば「1.10」を「110」に変換し、値を100倍に変換する
 
ans = a*b // 100
 
print(ans)
