class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) < 2:
            return int(tokens[-1])
        stack = []

        def operate(o, a, b):
            if o == '+':
                return a + b
            elif o == '-':
                return a - b
            elif o == '*':
                return a * b
            else:
                return int(a / b)
        for i in range(len(tokens)):
            if tokens[i] in '+-*/':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(operate(tokens[i], a, b))
            else:
                stack.append(tokens[i])
        return stack[-1]