#k층 n호
T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())

    arr = []

    for i in range(n):
        arr[i] = i + 1
     
print(arr)
# arr = [[0] * 3 for _ in range(6)]
# arr[2][1] = 10 2층 2호
# print(arr)
