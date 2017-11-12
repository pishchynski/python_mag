import operator


def replace_unary_operators(expr):
    i = 1
    new_expr = ""
    if expr[0] == '-':
        new_expr += '0-'
    elif expr[0] in "0123456789(":
        new_expr += expr[0]

    while i < len(expr):
        if expr[i] == '-' and expr[i - 1] not in "0123456789":
            new_expr += '0-'
        elif expr[i] == '+' and expr[i - 1] not in "0123456789":
            i += 1
            continue
        else:
            new_expr += expr[i]
        i += 1
    return new_expr


def infix_to_postfix(expr):
    priority = {'**': 4, '*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
    stack = []
    postfix = []
    i = 0
    while i < len(expr):
        sym = expr[i]
        if sym == '*' and expr[i + 1] == '*':
            sym = '**'
            i += 1
        if sym in priority.keys():
            if sym != '(':
                while (len(stack) != 0) and (priority[stack[-1]] >= priority[sym]):
                    postfix.append(stack.pop())
                stack.append(sym)
            else:
                stack.append(sym)
        elif sym == ')':
            top_token = stack.pop()
            while top_token != '(':
                postfix.append(top_token)
                top_token = stack.pop()
        else:
            j = i + 1
            while j < len(expr) and expr[j] in "0123456789.":
                sym += expr[j]
                j += 1
            i = j - 1
            postfix.append(sym)
        i += 1

    while len(stack) != 0:
        postfix.append(stack.pop())
    return " ".join(postfix)


def calc_postfix(expr):
    OPERATORS = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv, '**': operator.pow}
    stack = [0]
    for token in expr.split(" "):
        if token in OPERATORS:
            op2, op1 = stack.pop(), stack.pop()
            stack.append(OPERATORS[token](op1, op2))
        elif token:
            stack.append(float(token))
    return stack.pop()


def interpret(expr):
    expr = expr.replace(" ", "")
    expr = replace_unary_operators(expr)
    return calc_postfix(infix_to_postfix(expr))


if __name__ == '__main__':
    while True:
        expression = raw_input("Enter expression to calculate: \n")
        if not expression:
            exit(0)
        print interpret(expression)
