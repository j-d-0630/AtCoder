def function(N,A,B):
    num_list = []
    for i in range(1,N+1):
        num_list.append(str(i))
    
    sum_value = 0
    for i in range(0,len(num_list)):
        tmp = list(num_list[i])

        tmp2 = 0
        for j in tmp:
            tmp2 += int(j)
        
        if A <= tmp2 <= B:
            sum_value += int(num_list[i])
    
    return sum_value

tmp_inp = input()
tmp_inp2 = tmp_inp.split()
N = int(tmp_inp2[0])
A = int(tmp_inp2[1])
B = int(tmp_inp2[2])

ans = function(N,A,B)
print(ans)