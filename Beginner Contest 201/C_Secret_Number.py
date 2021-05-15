S = input()
ans = 0
for i in range(10000): #暗証番号0000～9999まで全てを評価する
  flag = [False]*10 # flg：0～9までのそれぞれが使用されているかどうかを示すリスト
  now = i #現在iを評価中
  for j in range(4): #暗証番号は4桁あるので4回ループで評価する
    flag[now%10] = True #下一桁の値を評価。⇒ flagをTrueにする
    now //= 10 #次の桁を評価するためnowを更新
  flag2 = True #flag2：評価した暗証番号が高橋くんの記憶Sに該当するかを示す
  for j in range(10): #Sを一文字ずつ見ていく
    if S[j] == "o" and not flag[j]: #S[j]がoなのにjという数字が使われていない場合は該当せず
      flag2 = False
    if S[j] == "x" and flag[j]: #S[j]がxなのにjという数字が使われている場合は該当せず
      flag2 = False
  ans += flag2
print(ans)