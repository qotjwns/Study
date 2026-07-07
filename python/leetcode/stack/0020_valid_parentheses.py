# LeetCode 20. Valid Parentheses
# Strategy: Stack
# Time: 
# Space: 

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for c in s:
            if c in "({[":
                stack.append(c)
            else:
                if not stack or stack.pop() != parentheses[c]:
                    return False
                
        return not stack