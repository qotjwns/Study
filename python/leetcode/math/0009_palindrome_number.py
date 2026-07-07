# LeetCode 9. Palindrome Number
# Strategy: Math / Reverse half of the number
# Time: O(log n)
# Space: O(1)


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        return x == reversed_half or x == reversed_half // 10


if __name__ == "__main__":
    solution = Solution()
    assert solution.isPalindrome(121) is True
    assert solution.isPalindrome(-121) is False
    assert solution.isPalindrome(10) is False
