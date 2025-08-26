w = str(input())

result = []

for a in w:
    if a.isupper():
        result.append(a.lower())
    else:
        result.append(a.upper())

print("".join(result))

# GPT
# s = input().strip()
# print(s.swapcase())