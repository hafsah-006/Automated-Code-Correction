def rpn_eval(tokens):
    def op(symbol, a, b):
        return {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b
        }[symbol](b, a)

    stack = []
 
    for token in tokens:
        if isinstance(token, float):
            stack.append(token)
        else:
            if len(stack) < 2:
                return "Error: Insufficient operands"
            a = stack.pop()
            b = stack.pop()
            if token == '/' and a == 0:
                return "Error: Division by zero"
            stack.append(
                op(token, a, b)
            )
    if len(stack) != 1:
        return "Error: Invalid expression"

    return stack.pop()
