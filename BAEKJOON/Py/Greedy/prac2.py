import sys
input = sys.stdin.readline

N, M = map(int, input().split())

result = 0

for _ in range(N):
    row = list(map(int, input().split()))
    row_min = min(row)
    result = max(row_min, result)
    
print(result)