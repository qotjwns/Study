#시간 초과 에러 sys.stdin.readlne 사용시 에러 해결
import sys
input = sys.stdin.readline
N = int(input())

stack = []
for _ in range(N):
    op = input().split()

    if op[0] == "push":
        stack.append(int(op[1]))

    elif op[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            num = stack.pop()
            print(num)

    elif op[0] == "size":
        print(len(stack))

    elif op[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif op[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])




#GPT
# import sys
# input = sys.stdin.readline

# N = int(input())
# stack = []
# out = []

# for _ in range(N):
#     op = input().split()
#     cmd = op[0]

#     if cmd == "push":
#         stack.append(int(op[1]))

#     elif cmd == "pop":
#         out.append(str(stack.pop() if stack else -1))

#     elif cmd == "size":
#         out.append(str(len(stack)))

#     elif cmd == "empty":
#         out.append("0" if stack else "1")

#     elif cmd == "top":
#         out.append(str(stack[-1] if stack else -1))

# sys.stdout.write("\n".join(out))