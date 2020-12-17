import functools

fin = open('a16.in')
file = fin.read()
fin.close()

fields, my_ticket, tickets = file.split("\n\n")

ranges = []
dic = {}
for field in fields.split("\n"):
    name, values = field.split(":")
    dic[name] = []
    for value in values.split("or"):
        low, high = map(int, value.strip().split("-"))
        if high > len(ranges):
            ranges += [1] * (high + 1)
        for i in range(low, high + 1):
            ranges[i] = 0
        dic[name].append((low, high))
        

total = 0
tickets = tickets.split("\n")[1:]
valid_tickets = []
for ticket in tickets:
    values = list(map(int, ticket.split(",")))
    valid = True
    for value in values:
        invalid = ranges[value] * value
        if invalid != 0:
            total += 1
            valid = False
    if valid:
        valid_tickets.append(values)
print(invalid)

my_ticket = my_ticket.split("\n")[1]
my_ticket = list(map(int, my_ticket.split(",")))

fields = list(dic.keys())
possibilities = [[1] * len(my_ticket) for i in range(len(fields))]
mapping = {}
for field in fields:
    mapping[field] = None

def validate(ranges, value):
    for low, high in ranges:
        if low <= value <= high: return True
    return False
    
for ticket in valid_tickets:
    for j in range(len(ticket)):
        value = ticket[j]        
        for i in range(len(fields)):
            ranges = dic[fields[i]]
            if not validate(ranges, value):
                possibilities[j][i] = 0

while not all(map(lambda x: sum(x) == 1, possibilities)):
    for i in range(len(possibilities)):
        possibility = possibilities[i]
        if sum(possibility) == 1:
            idx = possibility.index(1)
            for j in range(len(possibilities)):
                if i == j: continue
                possibilities[j][idx] = 0
mapping = {}
for i in range(len(possibilities)):
    idx = possibilities[i].index(1)
    mapping[i] = fields[idx]

product = 1
for i in range(len(my_ticket)):
    value = my_ticket[i]
    idx = possibilities[i].index(1)
    field = fields[idx]
    if 'departure' in field:
        product *= value
print(product)
    
    
