"""
整数で処理して誤差を無くす
if math.log2(a) < b * math.log2(c): を素直に計算すると小数点の誤差により、WAになる場合がある
よって整数で処理することで対応する
"""
a,b,c = map(int,input().split())

#math.log2(a) < b * math.log2(c)の判定は、a < c ** b と同じ
if a < c ** b:
  print("Yes")
else:
  print("No")