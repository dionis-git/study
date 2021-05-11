list1 = ['To', 'be', 'or', 'not', 'to', 'be']
list2 = ['that', 'is', 'the', 'WHAT?']

print(f'The first list is {list1},\n'
      f'the second element of this list is "{list1[1]}".\n')

print(f'The second list is {list2}.')
list2[-1] = input("Let's change the last element of second list, enter something:\n")
print(f'Done! Now the second list is {list2},\n')

list_sum = list1 + list2
print(f'The sum of lists is "{list_sum = }"\n')

list_slice = list_sum[(len(list_sum) // 2 - 3): (len(list_sum) // 2 + 3)]
print(f'The slice of the summary list is "{list_slice = }"\n')
