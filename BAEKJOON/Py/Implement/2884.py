H, M = map(int, input().split())

miniute = H * 60 + M

miniute -= 45

if miniute < 0:
    miniute += 1440

adjust_H = miniute // 60
adjust_M = miniute % 60

print(adjust_H, adjust_M)
