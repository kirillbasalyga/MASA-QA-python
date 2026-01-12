inventory = ['apple', 'banana', 'orange', 'grape', 'pineapple', 'kiwi']
processed_items =[]
for index, item in enumerate(inventory, start=1):
    if index % 2 == 0 and len(item) > 5:
        processed_items.append(f'{index}. Удлиненный {item}')
        continue
    if index % 2 != 0 and item[0] in ('a', 'e', 'i', 'o', 'u'):
        processed_items.append(f'{index}. Стартует с гласной: {item}')
        continue
    processed_items.append(f'{index}. {item}')

print(inventory)
print(*processed_items, sep='\n')