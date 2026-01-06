N = 10
divide = 42

num_list = []
set_list = []

for _ in range(N):
    n = int(input())
    num_list.append(n)

for n in num_list:
    set_list.append(n % 42)

unique = list(set(set_list))
print(len(unique))