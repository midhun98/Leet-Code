class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        data = {}
        for index, number in enumerate(nums):
            if number in data and index - data[number] <= k:
                return True
            else:
                data[number] = index
        return False
