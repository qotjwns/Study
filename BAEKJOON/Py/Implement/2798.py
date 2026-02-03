#브루트포스

import sys
from itertools import combinations
input = sys.stdin.readline

R = 3


N, M = map(int, input().split())

cards = list(map(int, input().split()))

cur_sum = 0

for cards in list(combinations(cards, R)):

    check_sum = sum(cards)

    if check_sum > M:
        continue
    if cur_sum < check_sum:
        cur_sum = check_sum

print(cur_sum)