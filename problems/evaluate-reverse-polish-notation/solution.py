class Solution(object):
    def evalRPN(self, tokens):
        
        stack = []

        for ch in tokens:
            if ch not in {'+', '-', '*', '/'}:
                stack.append(ch)
            else:
                right = int(stack.pop())
                left = int(stack.pop())

                if ch == '+':
                    result = left + right
                elif ch == '-':
                    result = left - right
                elif ch == '*':
                    result = left * right
                else:
                    result = int(float(left) / right)

                stack.append(result)

        return int(stack[-1])