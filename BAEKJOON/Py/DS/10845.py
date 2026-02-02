import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
q = deque()

for _ in range(N):
    ops = input().split()
    cmd = ops[0]

    if cmd == "push":
        q.append(ops[1])

    elif cmd == "pop":
        print(q.popleft() if q else -1)

    elif cmd == "size":
        print(len(q))

    elif cmd == "empty":
        print(0 if q else 1)

    elif cmd == "front":
        print(q[0] if q else -1)

    elif cmd == "back":
        print(q[-1] if q else -1)