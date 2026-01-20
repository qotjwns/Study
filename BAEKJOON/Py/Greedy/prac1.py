import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

num_list = list(map(int, input().split()))
num_list.sort(reverse= -1)

first = num_list[0]
sec = num_list[1]


count = M // (K + 1)

'''
5 8 3
2 4 5 4 6
'''