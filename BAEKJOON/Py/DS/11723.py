import sys
input = sys.stdin.readline

M = int(input())
S = 0
ALL = (1 << 20) - 1

for _ in range(M):
    cmd = input().split()
    op = cmd[0]

    if op == "add":
        x = int(cmd[1])
        S |= (1 << (x - 1))

    elif op == "remove":
        x = int(cmd[1])
        S &= ~(1 << (x - 1))

    elif op == "check":
        x = int(cmd[1])
        print(1 if (S & (1 << (x - 1))) else 0)

    elif op == "toggle":
        x = int(cmd[1])
        S ^= (1 << (x - 1))

    elif op == "all":
        S = ALL

    elif op == "empty":
        S = 0