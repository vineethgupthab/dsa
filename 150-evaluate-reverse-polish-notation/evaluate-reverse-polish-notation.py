class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []; operations = ['+','-','*','/']
        for token in tokens:
            if token in operations:
                val1 = int(stack[-1])
                del stack[-1]
                val2 = int(stack[-1])
                del stack[-1]
                if token == '+':
                    stack.append(val2+val1)
                elif token == '-':
                    stack.append(val2-val1)
                elif token == '*':
                    stack.append(val2*val1)
                else:
                    stack.append(int(val2/val1))
            else:
                stack.append(int(token))
        return stack[-1]