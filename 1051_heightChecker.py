class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        sorted_height = sorted(heights)

        for i in range(len(heights)):
            if heights[i] != sorted_height[i]:
                count += 1
        return count
# 
