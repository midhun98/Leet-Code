# https://leetcode.com/problems/search-insert-position/
# explantion https://www.midhun98.in/blog-list/25/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[-1] < target:
            return len(nums)
        else:
            for index, num in enumerate(nums):
                if num == target:
                    return index
                if num > target:
                    return index
