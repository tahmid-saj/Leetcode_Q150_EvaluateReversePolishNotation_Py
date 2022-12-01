class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for i in tokens:
            if i not in "*+/-":
                stack.append(i)
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                if i == '+': stack.append(a+b)
                elif i == '-': stack.append((b-a))
                elif i == '*': stack.append(b*a)
                else: stack.append(b/a)
        
        return int(stack[-1])
