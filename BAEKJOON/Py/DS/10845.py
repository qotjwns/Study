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


'''
import sys
input = sys.stdin.readline

N = int(input())

q = []
head = 0  # 큐의 맨 앞 인덱스

for _ in range(N):
    ops = input().split()
    cmd = ops[0]

    if cmd == "push":
        q.append(ops[1])

    elif cmd == "pop":
        if head == len(q):
            print(-1)
        else:
            print(q[head])
            head += 1

    elif cmd == "size":
        print(len(q) - head)

    elif cmd == "empty":
        print(1 if head == len(q) else 0)

    elif cmd == "front":
        print(-1 if head == len(q) else q[head])

    elif cmd == "back":
        print(-1 if head == len(q) else q[-1])

    if head > 10000 and head * 2 > len(q):
        q = q[head:]
        head = 0
'''