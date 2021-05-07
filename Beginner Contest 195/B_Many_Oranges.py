import math

a,b,w = map(int,input().split())
upper = int(math.floor(1000*w/a)) #切り捨て
lower = int(math.ceil(1000*w/b)) #切り上げ

if lower > upper:
  print("UNSATIFIABLE")
else:
  print(lower,upper)

# A,B,W = map(int,input().split())

# max_v = int(W*1000/A)
# if W*1000%B == 0:
#   min_v = int(W*1000/B)
# else:
#   min_v = int(W*1000/B)+1

# rslt = "OK"

# if A == B:
#   if W*1000%A == 0:
#     print("{} {}".format(min_v,max_v))
#   else:
#     rslt = "UNSATISFIABLE"
#     print(rslt)

# else:
#   if (W*1000%A)/max_v > (B-A):
#     rslt = "UNSATISFIABLE"

#   if (min_v*B - W*1000)/min_v > (B-A):
#     rslt = "UNSATISFIABLE"

#   if rslt == "OK":
#     print("{} {}".format(min_v,max_v))
#   else:
#     print(rslt)
