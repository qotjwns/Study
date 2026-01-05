import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

NUM = str(A * B * C)

num_count_list = [0 for _ in range(10)]

for i in NUM:
    num_count_list[int(i)] += 1

for num in num_count_list:
    print(num)