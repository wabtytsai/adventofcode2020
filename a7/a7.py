from functools import lru_cache

fin = open('a7.in')

rules = fin.readlines()

dic = {}
for rule in rules:
    # string splicing magic
    root, rest = rule.split(" bags contain ")
    dic[root] = []
    bags = rest.split(", ")
    for bag in bags:
        bag = bag.strip().strip('.')
        idx = bag.find(" ")
        quantity, bag = bag[:idx], bag[idx + 1:]
        bag = bag[:-5] if bag[-1] == 's' else bag[:-4]
        if quantity == 'no':
            break
        quantity = int(quantity)
        dic[root].append((quantity, bag))

@lru_cache(maxsize=256)
def find(bag):
    if bag == 'shiny gold':
        return True
    contents = dic[bag]
    for (quantity, content) in contents:
        if find(content) == True:
            return True
    return False

@lru_cache(maxsize=256)
def count(bag):
    contents = dic[bag]
    if len(contents) == 0: return 0
    total = 0
    for (quantity, content) in contents:
        total += (1 + count(content)) * quantity
    return total
    

total = 0
for i in dic.keys():
    if find(i) == True:
        total += 1
print(total - 1)
print(count('shiny gold'))

fin.close()
