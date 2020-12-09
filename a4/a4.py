fin = open('a4.in')

passports = fin.read().split("\n\n")
total = 0
for x in range(len(passports)):
    passport = passports[x]
    valid = {
        'byr': 0,
        'iyr': 0,
        'eyr': 0,
        'hgt': 0,
        'hcl': 0,
        'ecl': 0,
        'pid': 0,
    }
    items = []
    for i in passport.split("\n"):
        items += i.split(" ")
    for item in items:
        field, value = item.split(":")
        if (field == 'cid'):
            continue
        elif (field == 'byr'):
            value = eval(value)
            valid[field] = 1920 <= value <= 2002
        elif (field == 'iyr'):
            value = eval(value)
            valid[field] = (2010 <= value <= 2020)
        elif (field == 'eyr'):
            value = eval(value)
            valid[field] = (2020 <= value <= 2030)
        elif (field == 'hgt'):
            if ('in' in value):
                value = int(value[:value.find('in')])
                valid[field] = 59 <= value <= 76
            elif ('cm' in value):
                value = int(value[:value.find('cm')])
                valid[field] = 150 <= value <= 193
        elif (field == 'hcl'):
            if (value[0] != '#'):
                continue
            if (len(value) != 7):
                continue
            value = value[1:]
            color = True
            for i in value:
                if i not in '0123456789abcdef':
                    color = False
            valid[field] = color
        elif (field == 'ecl'):
            valid[field] = value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        elif (field == 'pid'):
            if (len(value) != 9):
                continue
            num = True
            for i in value:
                if i not in '0123456789':
                    num = False
            valid[field] = num
        
    if (sum(valid.values()) == 7):
        total += 1
print(total)
    
        

fin.close()
