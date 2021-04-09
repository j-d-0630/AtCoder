def function(N,input_data):
  count = 0

  prel_max_v = max(input_data)
  input_data.pop(input_data.index(prel_max_v))
  count += 1

  for i in range(N-1):
    max_v = max(input_data)

    if max_v < prel_max_v:
      input_data.pop(input_data.index(max_v))
      count += 1
      prel_max_v = max_v
    
    else:
      input_data.pop(input_data.index(max_v))
  
  return count


N = int(input())
input_data = []

for i in range(N):
  tmp = input()
  input_data.append(int(tmp))

ans = function(N,input_data)
print(ans)