def function(input_data):
  count = 0
  while(1):
    for i in range(0,len(input_data)):
      if input_data[i]%2 != 0:
        return count

      input_data[i] /= 2
    
    count += 1


tmp = input()
tmp2 = input()
tmp3 = tmp2.split()

input_data = []
for i in range(0,int(tmp)):
  input_data.append(int(tmp3[i]))

ans = function(input_data)
print(ans)