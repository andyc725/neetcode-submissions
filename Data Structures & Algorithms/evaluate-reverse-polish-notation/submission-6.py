class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for t in tokens:
            if t.isdigit() or "-" in t and t != "-":
                stack.append(int(t))
            elif t == "+": 
                res = stack.pop() + stack.pop()
                stack.append(res)
                
            elif t == "-":
                r1 = stack.pop()
                r2 = stack.pop() 
                res = r2 - r1
                stack.append(res)
               
                
            elif t == "*": 
                res = stack.pop() * stack.pop()
                stack.append(res)
                
            elif t == "/": 
                r1 = stack.pop()
                r2 = stack.pop() 
                res = r2 / r1
                stack.append(int(res))
        return int(stack[0])
        '''
        actual = []
        res = ""
        for i in range(len(tokens)):
            if tokens[i].isdigit():
                actual.append(int(tokens[i]))
                #actual.insert(-2, "(")
            else:
                #actual.insert(-3, "(")
                actual.insert(-1, tokens[i])
                #actual.insert(-3, "(")
                actual.append(")")
        
        print(actual)
        '''