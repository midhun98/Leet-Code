class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        while n not in visit:
            visit.add(n)
            n = self.sumofsquare(n)
            if n == 1:
                return True
        return False

    def sumofsquare(self, n):
        num = str(n)
        num = [int(i) * int(i) for i in num]
        return sum(num)
