import sys
input = sys.stdin.readline

N = int(input())
#[S, M, L, XL, XXL, XXL]
num_T = list(map(int, input().split()))
T, P = map(int, input().split())

max_order_T = 0
for i in num_T:
    if i % T == 0:
        max_order_T += (i // T)
    else:
        max_order_T+= (i // T) + 1

max_order_pen = 0
remain_order_pen = 0

max_order_pen = sum(num_T) // P
remain_order_pen = sum(num_T) % P




print(max_order_T)
print(max_order_pen, remain_order_pen)