import sys
input = sys.stdin.readline

def check(num: str) -> str:
    num_reverse = num[::-1]
    if num_reverse == num:
        return "yes"
    
    else: return "no"

if __name__ == "__main__":
    while True:
        number = str(input().strip())

        if number == "0":
            break

        print(check(number))
    