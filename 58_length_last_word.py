class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])

ss = Solution()
print(ss.lengthOfLastWord("   fly me   to   the moon  "))
