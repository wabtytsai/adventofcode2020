
def seatToNum(line):
    line = line.replace("B", "1")
    line = line.replace("F", "0")
    line = line.replace("R", "1")
    line = line.replace("L", "0")
    return int(line, 2)

fin = open('a5.in')

seats = []

for line in fin.readlines():
    seat = seatToNum(line)
    seats.append(seat)
    

low = min(seats)
high = max(seats)
for i in range(low, high):
    if (i not in seats):
        print (i)

fin.close()
