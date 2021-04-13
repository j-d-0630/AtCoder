def function(N,input_data):
    for i in range(N):
        dist = abs(input_data[i][1]-input_data[i+1][1])+abs(input_data[i][2]-input_data[i+1][2])
        time = abs(input_data[i][0]-input_data[i+1][0])
        
        if (time-dist)%2 != 0 or (time-dist)<0:
            rslt = "No"
            break

        if i == (N-1):
            rslt = "Yes"

    return rslt


input_data = [[0,0,0]]
N = int(input())
for i in range(N):
    t,x,y = map(int,input().split())
    input_data.append([t,x,y])

ans = function(N,input_data)
print(ans)