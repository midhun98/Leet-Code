import re
class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        s = s.strip()
        match = re.match(r'^[+-]?\d+', s)
        if match:
            num = int(match.group(0))
            if num < INT_MIN:
                return INT_MIN
            elif num > INT_MAX:
                return INT_MAX
            else:
                return num
        else:
            return 0
