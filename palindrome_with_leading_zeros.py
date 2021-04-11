def function(N):
    N_list = list(N)

    if len(N) == 1:
        return "Yes"
    
    flg = 0
    for i in range(0,int(len(N_list)/2)):
        if N_list[i] != N_list[len(N_list)-1-i]:
            flg = 1
        
    if flg == 0:
        return "Yes"
    
    while(1):
        if N_list[len(N_list)-1] != '0':
            break

        flg = 0
        N_list.pop(len(N_list)-1)
        for i in range(0,int(len(N_list)/2)):
            if N_list[i] != N_list[len(N_list)-1-i]:
                flg = 1
        
        if flg == 0:
            return "Yes"
    
    return "No"


N = str(input())
ans = function(N)
print(ans)