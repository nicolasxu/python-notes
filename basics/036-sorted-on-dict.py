inventory = ['Axe', 'Great Sword', 'Stick']

rarity = {
    'Great Sword': 98,
    'Golden Bow': 92,
    'Iron Sword': 80,
    'Axe': 34,
    'Stick': 2
}


sorted_inv = sorted(inventory, key=rarity.__getitem__, reverse=False)
print(sorted_inv)