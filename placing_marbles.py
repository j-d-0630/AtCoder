def function(text):
  count = 0
  text_2 = list(text)
  for i in text_2:
    if i == "1":
      count += 1
  
  return count

inputdata = input()
ans = function(inputdata)
print(ans)