T = int(input())

for _ in range(T):
    output = ""
    repeat, str = input().split()
    repeat = int(repeat)

    for alphabet in str:
        output = output + (alphabet * repeat)

    print(output)


#GPT
# import sys
# input = sys.stdin.readline

# T = int(input())
# for _ in range(T):
#     r, s = input().split()
#     r = int(r)
#     print(''.join(ch * r for ch in s))