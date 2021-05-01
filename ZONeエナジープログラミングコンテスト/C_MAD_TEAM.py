N = int(input())
A = [tuple(map(int,input().split())) for i in range(N)]

def check(x):
  s = set()
  for a in A:
    #x以上の場合、bit演算した値を加算していく（A~Eまで全てx以上なら、1+2+4+8+16⇒31となる）
    s.add(sum(1 << i for i in range(5) if a[i] >= x))
  #全組み合わせを計算
  for x in s:
    for y in s:
      for z in s:
        #A,B,C,D,E全ての項目でx以上となる組み合わせの場合は31となる
        if x | y | z == 31:
          return True
  return False

ok = 0
ng = 10**9 + 1
while ng - ok > 1:
  cen = (ok + ng)//2
  if check(cen):
    ok = cen
  else:
    ng = cen
print(ok)