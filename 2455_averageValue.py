# Explanation - https://www.midhun98.in/blog-list/24/
# problem- https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/description/

from typing import List
import statistics


class Solution:
    def averageValue(self, nums: List[int]) -> int:
        even_list = [i for i in nums if i % 2 == 0]
        three_list = [i for i in even_list if i % 3 == 0]
        try:
            return int(statistics.mean(three_list))
        except:
            return 0


ss = Solution()
print(ss.averageValue([1, 2, 4, 7, 10]))
