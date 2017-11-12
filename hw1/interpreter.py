import operator


def infix_to_postfix(expr):
    priority = {'**': 4, '*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
    stack = []
    postfix = []
    i = 0
    at_start = True
    while i < len(expr):
        sym = expr[i]
        if sym == '*' and expr[i + 1] == '*':
            sym = '**'
            i += 1
        if sym == ' ':
            i += 1
            continue
        elif sym in priority.keys():
            if sym != '(':
                if sym == '-' and at_start:
                    postfix.append('~')
                    stack.pop()
                else:
                    while (len(stack) != 0) and (priority[stack[-1]] >= priority[sym]):
                        postfix.append(stack.pop())
            else:
                at_start = True
            stack.append(sym)
        elif sym == ')':
            top_token = stack.pop()
            while top_token != '(':
                postfix.append(top_token)
                top_token = stack.pop()
        else:
            at_start = False
            j = i + 1
            if j < len(expr):
                while expr[j] in "0123456789.":
                    sym += expr[j]
                    j += 1
                i = j - 1
            postfix.append(sym)
        i += 1

    while len(stack) != 0:
        postfix.append(stack.pop())
    return " ".join(postfix)


def calc_postfix(expr):
    OPERATORS = {'+': operator.add, '-': operator.sub, '~': operator.sub, '*': operator.mul, '/': operator.truediv, '**': operator.pow}
    stack = [0]
    for token in expr.split(" "):
        if token in OPERATORS:
            if token == '~':
                op2, op1 = stack.pop(), 0
            else:
                op2, op1 = stack.pop(), stack.pop()
            stack.append(OPERATORS[token](op1, op2))
        elif token:
            stack.append(float(token))
    return stack.pop()


def interpret(expr):
    postfix_sooqa = infix_to_postfix(expr)
    print postfix_sooqa
    return calc_postfix(postfix_sooqa)


if __name__ == '__main__':
    while (True):
        expr = raw_input("Enter expression to calculate: \n")
        if not expr:
            exit(0)
        print interpret(expr)
