S = list(input())
ans = {"a": -1, "b": -1, "c": -1, "d": -1, "e": -1, "f": -1, "g": -1, "h": -1, "i": -1, "j": -1, "k": -1, "l": -1, "m": -1, "n": -1, "o": -1, "p": -1, "q": -1, "r": -1, "s": -1,
       "t": -1, "u": -1, "v": -1, "w": -1, "x": -1, "y": -1, "z": -1}

for index, s in enumerate(S):
    if ans[s] == -1:
        ans[s] = index

print(*ans.values())


##GPT
# S = input().strip()
# ans = [-1] * 26

# for i, ch in enumerate(S):
#     idx = ord(ch) - ord('a')
#     if ans[idx] == -1:
#         ans[idx] = i

# print(*ans)