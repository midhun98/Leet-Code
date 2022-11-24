# https://leetcode.com/problems/single-number/description/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count_dict = {}
        for index, num in enumerate(nums):
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 0
        return min(count_dict, key=count_dict.get)
