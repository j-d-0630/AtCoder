S = input()
divide = ["dream","dreamer","erase","eraser"]
divide_2 = []

for i in range(0,len(divide)):
    divide_2.append(divide[i][::-1])

S_2 = S[::-1]

while(1):
    rslt = None
    flg = 0
    for i in range(0,len(divide_2)):
        for j in range(0,len(divide_2[i])):
            if divide_2[i][j] != S_2[j]:
                break

            if j == len(divide_2[i])-1:
                flg = 1
        
        if flg == 1:
            tmp = i
            break

        if i == len(divide_2)-1:
            rslt = "NO"
            break
    
    if rslt == "NO":
        break

    rslt = "YES"
    S_2 = S_2[len(divide_2[i]):]
    
    if len(S_2) == 0:
        break

print(rslt)