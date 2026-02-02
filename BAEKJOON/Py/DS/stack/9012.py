#O(TL)

import sys
input = sys.stdin.readline

T = int(input())

def check_VPS(line: str) -> str:
    stack = []
    for s in line:
        if s == "(":
            stack.append(s)
        elif s == ")":
            try:
                stack.pop()
            except:
                return "NO"
    
    return "YES" if not stack else "NO"

if __name__ == "__main__":
    for _ in range(T):
        PS = str(input())
        print(check_VPS(PS))


'''
import sys
input = sys.stdin.readline

T = int(input())

def check_VPS(line: str) -> str:
    stack = []
    for s in line.strip():
        if s == "(":
            stack.append(s)
        elif s == ")":
            if stack:
                stack.pop()
            else:
                return "NO"
    return "YES" if not stack else "NO"

if __name__ == "__main__":
    for _ in range(T):
        PS = input()
        print(check_VPS(PS))
'''