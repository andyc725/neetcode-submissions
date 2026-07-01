class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {"(": ")", "[": "]", "{": "}"}

        for c in s:
            if c in closeToOpen.keys():
                stack.append(c)
            elif len(stack) != 0 and c == closeToOpen[stack[len(stack) - 1]]:
                stack.pop()
            else:
                return False
        
        if len(stack) == 0:
            return True
        else:
            return False