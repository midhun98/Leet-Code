class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        paranthesis = {'}': '{', ')': '(', ']': '['}
        stack = []
        for i in s:
            if i in paranthesis:
                if stack and stack[-1] == paranthesis[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False
