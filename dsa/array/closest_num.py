# https://leetcode.com/problems/find-closest-number-to-zero/description/
# Given an integer array nums of size n, return the number with the value closest to 0 in nums.
# If there are multiple answers, return the number with the largest value.

class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        closest_num = nums[0]
        for i in nums:
            if abs(closest_num) > abs(i):
                closest_num = i

        if abs(closest_num) in nums:
            return abs(closest_num)
        return closest_num

sol = Solution()

print(sol.findClosestNumber([-4,-2,1,4,8]))
print(sol.findClosestNumber([2,-1,1]))
