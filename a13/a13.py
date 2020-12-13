fin = open('a13.in')

timestamp = int(fin.readline())
lines = fin.readline().split(',')
buses = []
for bus in lines:
    if bus == 'x': continue
    buses.append(int(bus))


ID = max(buses)
earliest = timestamp * ID

def calc(start, bus):
    diff = start % bus
    if diff == 0: return start
    return start + bus - diff

for bus in buses:
    time = calc(timestamp, bus)
    if time < earliest:
        earliest = time
        ID = bus
print(ID * (earliest - timestamp ))

from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
  
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

n = []
a = []
count = 0
for bus in lines:
    if bus != 'x':
        n.append(int(bus))
        a.append(count)
    count -= 1
print(chinese_remainder(n, a))
fin.close()
