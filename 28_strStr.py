class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_needle = len(needle)
        len_haystack = len(haystack)+1-len_needle
        for i in range(len_haystack):
            if haystack[i:i+len_needle] == needle:
                return i
        return -1
