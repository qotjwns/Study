YEAR = int(input())


if YEAR % 400 == 0:
    print(1)
elif YEAR % 100 == 0:
    print(0)
elif YEAR % 4 == 0:
    print(1)
else:
    print(0)