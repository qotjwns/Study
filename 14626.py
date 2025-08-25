# check test case
# num = str(9788968322273)
# check_sum = 0
# for i in range(len(str(num))):
#     if int(num[i]) % 2 == 0:
#         check_sum += int(num[i])
#     else:
#         check_sum += 3 * int(num[i])

# print(check_sum % 10)

ISBN_SIZE = 13

num = str(input())
check_sum = 0
loc_missing = None

for i in range(ISBN_SIZE):
    if num[i] == "*":
        loc_missing = i
        continue
    elif i % 2 == 0:
        check_sum += int(num[i])
    else:
        check_sum += 3 * int(num[i])


if loc_missing % 2 == 0:
    sol = (((check_sum // 10) + 1) * 10 ) - check_sum # 
    print(sol)
else:
    for i in range(10):
        if (check_sum + 3 * i) % 10 == 0:
            print(i)
            break

# GPT
# def solve():
#     num = input().strip()
#     check_sum = 0
#     pos = None
    
#     for i, ch in enumerate(num):
#         if ch == "*":
#             pos = i
#             continue
#         d = int(ch)
#         if i % 2 == 0:
#             check_sum += d
#         else:
#             check_sum += 3 * d
    
#     if pos % 2 == 0:  # 짝수 자리
#         digit = (10 - (check_sum % 10)) % 10
#         print(digit)
#     else:  # 홀수 자리
#         for d in range(10):
#             if (check_sum + 3 * d) % 10 == 0:
#                 print(d)
#                 break

# if __name__ == "__main__":
#     solve()