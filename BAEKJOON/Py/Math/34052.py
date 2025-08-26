L = 4
sum = 0

for _ in range(L):
    t = int(input())
    sum += t

if (sum + 300) <= 1800:
    print("Yes")
else:
    print("No")