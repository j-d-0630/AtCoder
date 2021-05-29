import bisect
import sys
input = sys.stdin.readline

#深さ優先探索
# G:隣接リスト, root:0
def euler_tour(G,root):
  n = len(G)
  depth_list = [] #各depthに入った時刻を示すリスト
  entry_id = [-1]*n #各nodeに入った時刻
  exit_id = [-1]*n #各nodeを出ていった時刻

  v = root #探索中のnode
  it = [0]*n # そのnodeの子を何個目まで探索したか。→子が3個いるならばit=3までカウントアップされた時に探索終了させるのに使用する
  parents = [-1]*n # 各nodeの親nodeを示すリスト
  visit_id = 0 # node間を移動した回数。→各行動時刻を管理するために使う
  depth = 0 # 現在いる深さ
  while v != -1: #深さ優先探索が終了するまで続ける
    if entry_id[v] == -1: #そのnodeに来た事がないならTrue
      entry_id[v] = visit_id
      if len(depth_list) <= depth: #現在の深さがdepth_listよりも深いなら、リストを追加する
        depth_list.append([])
      depth_list[depth].append(visit_id) #そのdepthに入った時刻を記録
      visit_id += 1
    
    g = G[v]
    if it[v] == len(g): # 子node全てを探索し切ったらTrue
      exit_id[v] = visit_id # 出ていった時刻を記録
      v = parents[v] # 一つ上のnodeに戻るためにvを親nodeに変更
      depth -= 1 # 深さを上流に変更
      visit_id += 1
    else:
      child = g[it[v]] #gはvの子リスト。まずはg[0]から探索していく
      parents[child] = v
      it[v] += 1 # 深さ方向の探索が終わった後に隣の子であるg[1]を探索できるようにインクリメントしておく
      v = child # 探索中のnodeを子nodeに設定
      depth += 1 #depthを深くする
  
  return entry_id, exit_id, depth_list


#ent:Uに入った時刻。exit:Uを出ていった時刻。x:D
#ent～exitの時間にdepth_list[x]が何個あるかが解となる
def count(ent,exit,x):
  global size
  global depth_list
  if x >= size:
    return 0
  else:
    s = bisect.bisect_left(depth_list[x],ent)
    t = bisect.bisect_right(depth_list[x],exit,s) #s以上の範囲を対象とする
    return t - s


N = int(input())
es = [[] for _ in range(N)]
P = map(int,input().split())
#隣接リストの作成(各nodeはどのnodeの子か)
for u, v in enumerate(P,1):
  es[v-1].append(u)
  #es = [[node1の子のnode_idが加えられたリスト],[node2の・・・],[node3の・・・],[],,,]

entry_id, exit_id, depth_list = euler_tour(es,0)
size = len(depth_list) # depthの大きさ

Q = int(input())
ans = [0]*Q
for i in range(Q):
  U,D = map(int,input().split())
  ent = entry_id[U-1]
  exit = exit_id[U-1]
  ans[i] = count(ent,exit,D)

print(*ans)