class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 1 or n == 2:
            return 1
        elif n == 0:
            return 0
        elif n == 3:
            return 2
        else:
            n1 = 0
            n2 = 1
            n3 = 1
            for i in range(n):
                n4 = n1+n2+n3
                n1 = n2
                n2 = n3
                n3 = n4
        return n1
