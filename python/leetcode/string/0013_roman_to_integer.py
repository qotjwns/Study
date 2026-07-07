# LeetCode 13. Roman to Integer
# Strategy: String parsing / Hash Map
# Time: O(n)
# Space: O(1)

class Solution:
    def romanToInt(self, s:str) -> int:
        romans = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += romans[char]
        return number

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         values = {
#             "I": 1,
#             "V": 5,
#             "X": 10,
#             "L": 50,
#             "C": 100,
#             "D": 500,
#             "M": 1000,
#         }

#         total = 0
#         for i, char in enumerate(s):
#             value = values[char]
#             if i + 1 < len(s) and value < values[s[i + 1]]:
#                 total -= value
#             else:
#                 total += value

#         return total


# if __name__ == "__main__":
#     solution = Solution()
#     assert solution.romanToInt("III") == 3
#     assert solution.romanToInt("LVIII") == 58
#     assert solution.romanToInt("MCMXCIV") == 1994
