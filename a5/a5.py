
def seatToNum(line):
    line = line.replace("B", "1")
    line = line.replace("F", "0")
    line = line.replace("R", "1")
    line = line.replace("L", "0")
    return int(line, 2)

def numToSeat(num):
    line = bin(num)[2:]
    seat = ""
    for i in range(7):
        if (line[i] == '1'):
            seat += 'B'
        else:
            seat += 'F'
    for i in range(7, 10):
        if (line[i] == '1'):
            seat += 'R'
        else:
            seat += 'L'
    return seat

fin = open('a5.in')

seats = []
highest = 9

for line in fin.readlines():
    seat = seatToNum(line)
    highest = max(seat, highest)
    seats.append(seat)
    
    
##    low = 0
##    high = 127
##    for i in range(7):
##        if (line[i] == 'F'):
##            high = (low + high - 1) // 2
##        else:
##            low = (low + high + 1) // 2
##    row = int(low)
##    low = 0
##    high = 7
##    for i in range(7, 10):
##        if (line[i] == 'L'):
##            high = (low + high - 1) // 2
##        else:
##            low = (low + high + 1) // 2
##            
##    column = low
##
##    seat = (row * 8 + column)
##    seats[seat] = line

low = min(seats)
high = max(seats)
for i in range(low, high):
    if (i not in seats):
        print (i)

fin.close()
