fin = open('a8.in')

lines = fin.readlines()

idx = 0
acc = 0
mem = {}

while True:
    if idx in mem:
        break
    mem[idx] = True
    code, value = lines[idx].split(" ")

    if code == 'nop':
        idx += 1
        continue
    if code == 'acc':
        acc += eval(value)
        idx += 1
        continue
    if code == 'jmp':
        idx += eval(value)
        continue

def check(codes, i):
    if 'nop' in codes[i]:
        codes[i] = codes[i].replace('nop', 'jmp')
    elif 'jmp' in codes[i]:
        codes[i] = codes[i].replace('jmp', 'nop')
    idx = 0
    acc = 0
    mem = {}
    valid = False
    while True:
        if idx in mem:
            break
        if idx >= len(codes):
            valid = True
            break
        mem[idx] = True
        code, value = lines[idx].split(" ")

        if code == 'nop':
            idx += 1
            continue
        if code == 'acc':
            acc += eval(value)
            idx += 1
            continue
        if code == 'jmp':
            idx += eval(value)
            continue
    if 'nop' in codes[i]:
        codes[i] = codes[i].replace('nop', 'jmp')
    elif 'jmp' in codes[i]:
        codes[i] = codes[i].replace('jmp', 'nop')
    return (valid, acc)

for i in range(len(lines)):
    valid, acc = check(lines, i)
    if valid: print(valid, acc)
##print(acc)

fin.close()
