def find_operators(expr):
    ops = [':', '/', '*', '+', '-']
    return [(i, expr[i]) for op in ops for i in range(len(expr)) if expr[i] == op]

def get_operand(expr, idx, left=True):
    step = -1 if left else 1
    i, operand = idx + step, ''
    while 0 <= i < len(expr) and expr[i] not in "+-*/:=\0":
        if expr[i] != '$':
            operand = expr[i] + operand if left else operand + expr[i]
            expr[i] = '$'
            break
        i += step
    return operand

def intermediate_code(expr):
    expr = list(expr)
    tmpch = ord('Z')
    ops = find_operators(expr)
    print("The intermediate code:\t\tExpression")
    for pos, op in ops:
        l = get_operand(expr, pos, True)
        r = get_operand(expr, pos, False)
        expr[pos] = chr(tmpch)
        print(f"\t{chr(tmpch)} := {l}{op}{r}\t\t s = {''.join(c for c in expr if c != '$')}")
        tmpch -= 1
    print(f"\ts := {chr(tmpch + 1)}")

expr = input("Enter the Expression: ")
print("\n\t\tINTERMEDIATE CODE GENERATION\n")
intermediate_code(expr)
