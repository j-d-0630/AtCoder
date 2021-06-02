N = int(input())

ans = (pow(10,N) - (2*pow(9,N) - pow(8,N))) % 1000000007
print(ans)
