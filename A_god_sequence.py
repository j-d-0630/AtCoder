A,B = map(int,input().split())

def function(A,B):
    plu_l = []
    neg_l = []
    for i in range(1,A+1):
        plu_l.append(i)
    
    for i in range(-B,0):
        neg_l.append(i)
    
    while(1):
        tmp = sum(plu_l) + sum(neg_l)
        if tmp == 0:
            break
        
        if tmp > 0:
            neg_l[0] -= tmp
        
        if tmp < 0:
            plu_l[len(plu_l)-1] -= tmp

    rslt = []                
    [ rslt.append(neg_l[i]) for i in range(0,len(neg_l)) ]
    [ rslt.append(plu_l[i]) for i in range(0,len(plu_l)) ]
    return rslt

ans = function(A,B)
for i in range(len(ans)):
    print(ans[i]," ",end='')