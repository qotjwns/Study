import sys
input = sys.stdin.readline

S = set()
M = int(input())

def do_opr(opr: str, num: int | None = None):
    if opr == "add":
        S.add(num)
    elif opr == "remove":
        S.discard(num)  # 없어도 안전
    elif opr == "check":
        print(1 if num in S else 0)
    elif opr == "toggle":
        if num in S:
            S.remove(num)
        else:
            S.add(num)
    elif opr == "all":
        S.clear()
        S.update(range(1, 21))
    elif opr == "empty":
        S.clear()

if __name__ == "__main__":
    for _ in range(M):
        ops = input().split()
        if len(ops) == 2:
            do_opr(ops[0], int(ops[1]))
        else:
            do_opr(ops[0])


# 비트 마스킹
# import sys
# input = sys.stdin.readline

# M = int(input())
# S = 0
# ALL = (1 << 20) - 1

# for _ in range(M):
#     cmd = input().split()
#     op = cmd[0]

#     if op == "add":
#         x = int(cmd[1])
#         S |= (1 << (x - 1))

#     elif op == "remove":
#         x = int(cmd[1])
#         S &= ~(1 << (x - 1))

#     elif op == "check":
#         x = int(cmd[1])
#         print(1 if (S & (1 << (x - 1))) else 0)

#     elif op == "toggle":
#         x = int(cmd[1])
#         S ^= (1 << (x - 1))

#     elif op == "all":
#         S = ALL

#     elif op == "empty":
#         S = 0