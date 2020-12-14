fin = open('a14.in')
lines = []
for line in fin.readlines():
    lines.append(line)
fin.close()

def apply_mask(mask, value):
    value = "0" * (len(mask) - len(value)) + value
    result = ""
    for i in range(len(mask)):
        if mask[i] == 'X':
            result += value[i]
        else:
            result += mask[i]
    return result

mask = ""
mem = {}
for line in lines:
    if line[:4] == 'mask':
        mask = line.split("=")[1].strip()
        continue
    address, value = line.split("=")
    address = int(address.strip()[4:-1])
    value = bin(int(value))[2:]
    mem[address] = int(apply_mask(mask, value), 2)

print(sum(mem.values()))

def decode_address(mask, value):
    value = "0" * (len(mask) - len(value)) + value
    result = ""
    for i in range(len(mask)):
        if mask[i] == 'X':
            result += 'X'
        elif mask[i] == '1':
            result += '1'
        else:
            result += value[i]
    return result

def find_address(value):
    idx = value.find('X')
    if idx == -1:
        return [int(value, 2)]
    else:
        pre = value[:idx]
        suf = value[idx + 1:]
        return find_address(pre + '0' + suf) + find_address(pre + '1' + suf)

mem = {}
mask = ""
for line in lines:
    if line[:4] == 'mask':
        mask = line.split("=")[1].strip()
        continue
    address, value = line.split("=")
    address = bin(int(address.strip()[4:-1]))[2:]
    value = int(value)
    address = decode_address(mask, address)
    addresses = find_address(address)
    for address in addresses:
        mem[address] = value
print(sum(mem.values()))

