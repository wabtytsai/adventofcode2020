fin = open('a21.in')
lines = fin.readlines()
fin.close()

freq = {}
mapping = {}
items = set()

for menu in lines:
    menu = menu.strip()
    ingredients, allergens = menu.split(' (contains ')
    ingredients = set(ingredients.split(' '))
    items = items.union(ingredients)
    allergens = allergens[:-1].split(', ')

    for a in allergens:
        if a not in mapping:
            mapping[a] = ingredients
        else:
            mapping[a] = mapping[a].intersection(ingredients)
    for i in ingredients:
        if i not in freq:
            freq[i] = 0
        freq[i] += 1

done = False
while not done:
    done = True
    for allergen in mapping:
        if len(mapping[allergen]) > 1:
            done = False
            continue
        ingredient = list(mapping[allergen])[0]
        items.discard(ingredient)
        for a in mapping:
            if a == allergen: continue
            mapping[a].discard(ingredient)
        
print(sum([freq[i] for i in items]))
print(",".join([mapping[a].pop() for a in sorted(mapping.keys())]))
