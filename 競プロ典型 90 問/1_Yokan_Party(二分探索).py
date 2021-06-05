N,L = map(int,input().split())
K = int(input())
A_list = list(map(int,input().split()))

def solve(mid):
    pre = 0 #分割後の幅測定開始位置
    count = 0 #分割回数
    for i in range(N):
        #分割したものの左辺も右辺もmidより長いなら最長幅を更新できる条件を満たす
        if (A_list[i] - pre >= mid) and (L - A_list[i] >= mid):
            count += 1
            pre = A_list[i]
    
    if count >= K: # count分の分割で最長幅が更新できることが分かったが、この値がK以上でないと採用できない分け方となる
        return True
    else:
        return False

left = 0
right = L
while right - left > 1:
    mid = (right + left)//2
    if solve(mid) == False:
        right = mid # 以前のmidの左側の領域から答えを探す
    else:
        left = mid # 以前のmidの右側の領域から答えを探す

print(left)
