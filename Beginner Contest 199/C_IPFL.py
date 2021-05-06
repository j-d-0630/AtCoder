def main():
  n = int(input())
  s = list(input())
  q = int(input())
  
  t2_flag = False
  for _ in range(q):
    t,a,b = map(int,input().split())
    a -= 1 #indexに合わせるために-1する
    b -= 1 #indexに合わせるために-1する
    if t == 1:
      if t2_flag: #t==2が存在し前後入れ替えが起こっている場合は、それを踏まえた入れ替えの仕方を実施する
        if a < n and b < n: #aもbも文字列の前半分に存在する場合
          s[a+n],s[b+n] = s[b+n],s[a+n]
        elif a < n and n <= b:
          s[a+n],s[b-n] = s[b-n],s[a+n]
        elif n <= a and b < n:
          s[a-n],s[b+n] = s[b+n],s[a-n]
        else:
          s[a-n],s[b-n] = s[b-n],s[a-n]
      
      else: # 前後入れ替えが起こっていなければ、素直にs[a]とs[b]を交換する
        s[a],s[b] = s[b],s[a]
    
    if t == 2:
      if t2_flag:
        t2_flag = False
      else:
        t2_flag = True

  if t2_flag:
    s = s[n:] + s[:n]
  
  print("".join(s))


if __name__ == "__main__":
  main()