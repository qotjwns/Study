# 집합 사용 해쉬맵
import sys
input = sys.stdin.readline

N = int(input().strip())

A = set(map(int, input().split()))

M = int(input().strip())

test = list(map(int, input().split()))

for t in test:
    print(1) if t in A else print(0)