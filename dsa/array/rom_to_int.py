# https://leetcode.com/problems/roman-to-integer/description/

# convert roman number to integer


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rom_to_int = {
            "I": 1,
            "IV": 4,
            "IX": 9,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        subtracted_num = ["IV", "IX", "XL", "XC", "CD", "CM"]

        converted_num, index = 0, 0
        while index < len(s):
            if index+1 < len(s) and (s[index]+s[index+1]) in subtracted_num:
                converted_num += rom_to_int[s[index+1]] - rom_to_int[s[index]]
                index += 2
                continue

            converted_num += rom_to_int[s[index]]
            index += 1
        return converted_num

sol = Solution()
print(sol.romanToInt("III"))
print(sol.romanToInt("LVIII"))
print(sol.romanToInt("MCMXCIV"))
#  M = 1000, CM = 900, X = 10, XC = 90, IV = 4
