import functools

fin = open('a18.in')
lines = fin.readlines()
fin.close()

def do_math(expr, order):
    idx = expr.find('(')
    while idx >= 0:
        count = 0
        for i in range(len(expr)):
            if expr[i] == ')':
                count -= 1
                if count == 0:
                    break
            if expr[i] == '(':
                count += 1
        value = do_math(expr[idx + 1: i], order)
        expr = expr[:idx] + value + expr[i+1:]
        idx = expr.find('(')

    return order(expr)

def left_to_right(expr):
    a = ""
    for i in expr:
        if i == ' ': continue
        if i in '+*':
            a = '(' + a + ')'
        a += i
    return str(eval(a))

def add_first(expr):
    ops = expr.split("*")
    return str(functools.reduce(lambda a, b: a * b, map(eval, ops)))


print(sum(map(int, map(lambda a: do_math(a, left_to_right), lines))))
print(sum(map(int, map(lambda a: do_math(a, add_first), lines))))
