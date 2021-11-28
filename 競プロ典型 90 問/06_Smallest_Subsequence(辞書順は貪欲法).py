N,K = map(int,input().split())
S = input()

nex = [[0]*100001 for _ in range(26)]

for i in range(26):
  nex[i][len(S)] = len(S)
for i in range(len(S)-1,-1,-1):
  for j in range(26):
    if ord(S[i])-ord("a") == j:
      nex[j][i] = i
    else:
      nex[j][i] = nex[j][i+1]

ans = ""
CurrentPos = 0
for i in range(1,K+1): # K文字使うまでループ
  for j in range(26): # "a"が使用可能か、"b"が使用可能か,,,"z"が使用可能かを順番に調べる
    NexPos = nex[j][CurrentPos]
    MaxPosLength = len(S) - (NexPos + 1)
    if MaxPosLength >= K - i: # CurrentPos番目の文字をした場合の残り文字数がK以上個あれば採用可能
      ans += chr(ord("a") + j)
      CurrentPos = NexPos + 1 # S[NexPos]の文字を使用したので次はS[NexPos+1:N]の範囲の文字を対象に評価していく
      break # i番目の文字が確定したので、i+1番目の文字を決めていく

print(ans)