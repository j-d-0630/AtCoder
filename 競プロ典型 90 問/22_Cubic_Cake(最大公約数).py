"""
全てを同じ大きさに切るときに、切る回数を最小とできるカット長は各辺の最大公約数である
最大公約数はユークリッドの互除法で求まるが、pythonはmath.gcd()で計算できる
"""
import math
from functools import reduce

A,B,C = map(int,input().split())
gcd = reduce(math.gcd,[A,B,C]) # 最大公約数を計算 ※python3.9以降はmath.gcd()は引数を3個以上指定できるため、高階関数であるreduce()は不要

ans = (A//gcd - 1) + (B//gcd - 1) + (C//gcd - 1)

print(ans)