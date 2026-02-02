#O(n) stack

k = int(input())

arr = []

for _ in range(k):
    n = int(input())
    if n == 0:
        arr.pop()
    else:
        arr.append(n)


print(sum(arr))

#GPT
# import sys
# stack = []
# k = int(sys.stdin.readline())
# for _ in range(k):
#     num = int(sys.stdin.readline())
#     if num != 0:
#         stack.append(num)
#     else:
#         stack.pop()
# print(sum(stack))