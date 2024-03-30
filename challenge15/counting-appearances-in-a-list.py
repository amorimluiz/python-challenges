fruits = ['maca', 'banana', 'banana', 'maca', 'uva', 'pera', 'mexirica', 'maca', 'ameixa']
appearancesMap = {}

for fruit in fruits:
    if fruit not in appearancesMap:
        appearancesMap[fruit] = 0
    appearancesMap[fruit] += 1

print(appearancesMap)