import sys
input = sys.stdin.readline

def check(num: str) -> str:
    num_reverse = num[::-1]
    
    return "yes" if num_reverse == num else "no"

if __name__ == "__main__":
    while True:
        number = str(input().strip())

        if number == "0":
            break

        print(check(number))
    