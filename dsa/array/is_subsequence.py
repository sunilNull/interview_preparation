# https://leetcode.com/problems/is-subsequence/description/
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by
# deleting some (can be none) of the characters without disturbing the relative positions
# of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == "":
            return True
        if len(s) > len(t):
            return False
        index, new_str = 0, ""
        for i in t:
            if index < len(s) and i in s[index]:
                new_str += i
                index += 1
        
        return new_str == s

sol = Solution()
print(sol.isSubsequence("abc", "ahbgdc"))
print(sol.isSubsequence("axc", "ahbgdc"))
