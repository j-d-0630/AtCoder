N,L = map(int,input().split())
K = int(input())
A_list = list(map(int,input().split()))

# 解がmidより大きいか小さいかを探すための関数。大きければTrueを小さければFalseを返す
def solve(mid):
    pre = 0 #分割後の幅測定開始位置
    count = 0 #分割回数
    for i in range(N):
        #分割したものの左辺も右辺もmidより長いなら、この位置で分割した場合、midより大きな値を解にできる条件を満たす
        # A_list[i]で分割したときの左辺 and 右辺
        # ここで範囲を>=とするか>とするかで最後の解がleftになるかrightになるかが変わる。⇒midより大きいことを条件とすれば解はright、mid以上とすると解はleft。
        if (A_list[i] - pre >= mid) and (L - A_list[i] >= mid):
            count += 1
            pre = A_list[i]
    
    if count >= K: # count分の分割で最長幅が更新できることが分かったが、この値がK以上でないと採用できない分け方となる
        return True # 満たすならmidより大きな値の領域から解を探しに行く
    else:
        return False# 満たさないならmidより小さな値の領域から解を探しに行く

left = 0
right = L
while right - left > 1:
    mid = (right + left)//2
    if solve(mid) == False:
        right = mid # 以前のmidの左側の領域から答えを探す
    else:
        left = mid # 以前のmidの右側の領域から答えを探す

print(left)
