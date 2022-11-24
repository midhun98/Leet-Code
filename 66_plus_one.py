# url - https://leetcode.com/problems/plus-one/description/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        if digits[0] == 9 or len(digits) > 1:
            join = ''
            for i in digits:
                join += str(i)
            join = int(join) + 1
            final = eval(','.join(str(join)))
            final = list(final)
            return final

        elif len(digits) == 1:
            return [digits[0]+1]
