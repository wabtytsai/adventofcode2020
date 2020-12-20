
def seatToID(seat):
    number = ""
    for i in seat:
        if i in "BR":
            number += "1"
        elif i in "FL":
            number += "0"
    return int(number, 2)

fin = open('a5.in')

ids = set()

for line in fin.readlines():
    ids.add(seatToID(line))
    
high = max(ids)
low = min(ids)
print(high)
for i in range(low, high):
    if (i not in ids):
        print (i)

fin.close()
