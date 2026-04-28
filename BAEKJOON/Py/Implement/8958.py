import sys
input = sys.stdin.readline

N = int(input())
words = {input().strip() for _ in range(N)}  # 중복 제거

words = sorted(words, key=lambda x: (len(x), x))  # 길이 -> 사전순

print("\n".join(words))
