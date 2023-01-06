class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                if s[left+1:right+1] == s[left+1:right+1][::-1]:
                    return True
                elif s[left:right] == s[left:right][::-1]:
                    return True
                return False
            left += 1
            right -= 1
        return True
