import sys
input = sys.stdin.readline

notes = list(map(int, input().split()))

notes_sorted            = [1, 2, 3, 4, 5, 6, 7, 8]
notes_sorted_reverse    = [8, 7, 6, 5, 4, 3, 2, 1]

if notes == notes_sorted:
    print("ascending")
elif notes == notes_sorted_reverse:
    print("descending")
else:
    print("mixed")