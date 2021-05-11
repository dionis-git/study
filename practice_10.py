list1 = ['Homo', 'homini', 'lupus', 'est']
print(f'{list1 = }')

for word in list1:
    print(word)

for word in list1:
    for char in word:
        print(char, end='-')
    print()
print('\n')

list2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f'{list2 = }')

for i in range(len(list2)):
    list2[i] = float(i)
print(f'{list2 = }\n')
