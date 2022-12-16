class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_li = []
        for i in accounts:
            max_li.append(sum(i))
        return max(max_li)
