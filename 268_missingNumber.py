# https://leetcode.com/problems/missing-number/description/
# explanation - https://www.midhun98.in/blog-list/22/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = tuple(set(nums))
        if len(nums) == 1 and nums[0] != 0 or 0 not in nums:
            return 0
        small = min(nums)
        large = max(nums)
        for i in range(small, large):
            if i not in nums:
                return i
        return large+1
