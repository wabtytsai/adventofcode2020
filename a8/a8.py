fin = open('a8.in')

lines = fin.readlines()

def run(code):
    idx = 0
    acc = 0
    mem = set()

    while True:
        if idx in mem:
            return (acc, False)
        if idx >= len(code):
            return (acc, True)
        mem.add(idx)

        op, value = code[idx].split(" ")

        if op == 'nop':
            idx += 1
            continue
        if op == 'acc':
            acc += eval(value)
            idx += 1
            continue
        if op == 'jmp':
            idx += eval(value)
            continue

def check(code, i):
    temp = code[i]
    if 'nop' in code[i]:
        code[i] = code[i].replace('nop', 'jmp')
    elif 'jmp' in code[i]:
        code[i] = code[i].replace('jmp', 'nop')

    acc, valid = run(code)
    code[i] = temp
    return (valid, acc)

for i in range(len(lines)):
    valid, acc = check(lines, i)
    if valid: print(valid, acc)


fin.close()
