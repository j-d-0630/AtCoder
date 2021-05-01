N, D, H = map(int, input().split())
ans = 0.0
for i in range(N):
    d, h = map(int, input().split())
    h -= d * (H - h) / (D - d)
    if ans < h:
        ans = h
print(ans)
