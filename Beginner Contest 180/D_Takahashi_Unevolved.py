X,Y,A,B = map(int,input().split())
X_i = X

#Xを最小に変位させていくためには、最初はA倍で進み途中から+Bで進む。いつまでA倍かを求める。
count = 0
while X*(A-1) <= B:
  X += X*(A-1)
  count += 1

for i in range(count+1):
  if Y - X_i*A**i <= 0:
    ans = i-1
    print(ans)
    exit()


if (Y - X_i*A**count)%B != 0:
  ans = (Y - X_i*A**count)//B + count
else:
  ans = (Y - X_i*A**count)//B - 1 + count

print(ans)


#模範解答
# x,y,a,b=map(int,input().split())
# ans=0
# while a*x<=x+b and a*x<y:
#   x*=a
#   ans+=1
# print(ans+(y-1-x)//b)
