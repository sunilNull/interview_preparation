# https://leetcode.com/problems/merge-strings-alternately/
# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order,
# starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        new_str = ""
        max_len_str = max(len(word1), len(word2))
        for index in range(max_len_str+1):
            if len(word1) > index:
                new_str += word1[index]
            
            if len(word2) > index:
                new_str += word2[index]
        
        return new_str

sol = Solution()
print(sol.mergeAlternately("abc", "pqr"))
print(sol.mergeAlternately("ab", "pqrs"))
print(sol.mergeAlternately("abcd", "pq"))
