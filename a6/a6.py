fin = open('a6.in')

groups = fin.read().split("\n\n")

total = 0
for group in groups:
    size = group.count('\n') + 1
    count = {}
    # merge group into one line
    line = "".join(group.split('\n'))
    for i in line:
        if i not in count:
            count[i] = 0
        count[i] += 1
    for i in count.values():
        if i == size:
            total += 1

print(total)


fin.close()
