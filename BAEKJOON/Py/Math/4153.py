import sys
input = sys.stdin.readline

while True:
    A, B, C = map(int, input().split())
    ls = [A, B, C]
    ls.sort()

    if A == 0 and B == 0 and C == 0:
        break
    
    if ls[0] ** 2 + ls[1] ** 2 == ls[2] ** 2:
        print("right")
    else:
        print("wrong")