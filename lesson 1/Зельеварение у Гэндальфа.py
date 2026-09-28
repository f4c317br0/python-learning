def potions(line):
    with open('recipes.txt', 'r', encoding='utf8') as f:
        recipes = [el.split(',') for el in f.readlines()]
    recipes.reverse()
    for el in recipes:
        if line.lower() in el[0].lower():
            el[-1] = el[-1].strip('\n')
            return el[1:]
    return recipes


print(potions('Ти'))
