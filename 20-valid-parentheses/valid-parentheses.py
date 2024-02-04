class Solution:
    def isValid(self, s: str) -> bool:
        openclose = {'}':'{',')':'(',']':'['}
        stack = []
        for i in s:
            if stack and i in openclose:
                if openclose[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return False if stack else True
