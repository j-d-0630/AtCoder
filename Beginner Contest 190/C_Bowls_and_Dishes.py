import itertools

N,M = map(int,input().split())
cond = [tuple(map(int,input().split())) for i in range(M)] #condition(条件)
K = int(input())
choice = [tuple(map(int,input().split())) for i in range(K)] #皿にボール入れる人の選択肢

ans = 0

#choiceに対してデカルト積を生成
for balls in itertools.product(*choice):
    #set型にしてダブりを除外
    balls = set(balls)
    #cond内の(A,B)両方がballsに含まれていれば1となり、それをcond内に全て評価し加算していく
    cnt = sum(A in balls and B in balls for A, B in cond)
    #最大値を更新していく
    if ans < cnt:
        ans = cnt

print(cnt)
