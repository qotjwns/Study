NUM = 9

num_list = []
for _ in range(NUM):
    n = int(input())
    num_list.append(n)

max_val = max(num_list)

print(max_val)
print(num_list.index(max_val) + 1)
