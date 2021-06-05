N = int(input())

#カッコ列が正しいかどうかの判定方法は典型知識で以下の2条件を両方満たすこと
#条件1："("と")"の数が同じである
#条件2：左からi文字目までの時点で"("の数が")"の数以上である
def judge(S):
    dep = 0
    for i in range(len(S)):
        if S[i] == "(":
            dep += 1
        elif S[i] == ")":
            dep -= 1
        
        if dep < 0:
            return False
    if dep == 0:
        return True
    else:
        return False


#bit全探索
for i in range(1<<N): #2のN乗回ループする
    candidate = ""
    for j in range(N):
        if (i & (1 << (N-1-j))) == 0: #iを2進数表記したときのj+1bitの値が0ならば
            candidate += "("
        else:
            candidate += ")"
    
    rslt = judge(candidate)
    if rslt:
        print(candidate)