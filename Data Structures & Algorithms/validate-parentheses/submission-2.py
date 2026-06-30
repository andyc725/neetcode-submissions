class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2 != 0:
            return False

        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            else:
                if len(stack) == 0 or self.isOpposite(stack[len(stack) - 1], c) == False:
                    return False
                stack.pop()
        if len(stack) == 0:
            return True
        return False
    
    def isOpposite(self, c1: str, c2: str) -> bool:
        if (c1 == "{" and c2 == "}") or (c1 == "(" and c2 == ")") or (c1 == "[" and c2 == "]"):
            return True
        return False