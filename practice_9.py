def show_school():
    """Prints the dictionary 'school'"""
    print(f"Now the number of pupils in the school's classes is:")
    for cl in sorted(school):
        print(f'{cl} class - {school[cl]} pupils')
    print('\n')


def usr_func(choice):
    """Checks the user's choice and loads the needed function"""
    global school
    if choice == 1:
        while True:
            try:
                quantity = int(input('How many classes do you want to change? '))
                while not 0 < quantity <= len(school):
                    quantity = int(input(f'Enter the number from 1 to {len(school)}: '))
                else:
                    changed_school = change_class(quantity)
                    break
            except ValueError:
                print(f'Enter the number from 1 to {len(school)}.')
        for cls in school:
            if cls in changed_school:
                school[cls] = changed_school[cls]
        print('\nDone!', end=' ')
        show_school()
    elif choice == 2:
        while True:
            try:
                quantity = int(input('How many classes do you want to create? '))
                while not 0 < quantity <= len(school):
                    quantity = int(input(f'Enter the number from 1 to {len(school)}: '))
                else:
                    created_school = create_class(quantity)
                    break
            except ValueError:
                print(f'Enter the number from 1 to {len(school)}.')
        for cls in created_school:
            school[cls] = created_school[cls]
        print('\nDone!', end=' ')
        show_school()
    elif choice == 3:
        while True:
            try:
                quantity = int(input('How many classes do you want to disband? '))
                while not 0 < quantity <= len(school):
                    quantity = int(input(f'Enter the number from 1 to {len(school)}: '))
                else:
                    disbanded_school = disband_class(quantity)
                    break
            except ValueError:
                print(f'Enter the number from 1 to {len(school)}.')
        for cls in disbanded_school:
            if cls in school:
                del school[cls]
        print('\nDone!', end=' ')
        show_school()


def change_class(n):
    """Create dictionary with 'n' changed keys+values whose in 'school' dictionary (to change)"""
    i = 1
    changed = {}
    print(f"Let's change the number of pupils in any {n} classes.\n")
    while i <= n:
        is_changed = input(f'Enter the number of {i} class: ')
        while is_changed not in school:
            is_changed = input(f'There is no class {is_changed} in this school.\n'
                               f'Enter the number of {i} class: ')
            while is_changed in changed:
                is_changed = input(f'You are already select {is_changed} class.\n'
                                   f'Enter the number of {i} class: ')
        while is_changed in changed:
            is_changed = input(f'You are already select {is_changed} class.\n'
                               f'Enter the number of {i} class: ')
            while is_changed not in school:
                is_changed = input(f'There is no class {is_changed} in this school.\n'
                                   f'Enter the number of {i} class: ')
        is_changed_number = input(f'How many pupils now in {is_changed} class: ')
        while not is_changed_number.isdigit() or is_changed_number == school[is_changed]:
            is_changed_number = input(f'Enter the different positive number of pupils in {is_changed} class: ')
        changed[is_changed] = is_changed_number
        i += 1
    return changed


def create_class(n):
    """Create dictionary with 'n' new keys+values whose not in 'school' dictionary (to add)"""
    i = 1
    created = {}
    print(f"Let's create {n} new classes.\n")
    while i <= n:
        is_created = input(f'Enter the number of {i} class: ')
        while is_created in school or is_created in created:
            is_created = input(f'There is already class {is_created} in this school.\n'
                               f'Enter the number of {i} class: ')
        is_created_number = input(f'How many pupils now in {is_created} class: ')
        while not is_created_number.isdigit():
            is_created_number = input(f'Enter the positive number of pupils in {is_created} class: ')
        created[is_created] = is_created_number
        i += 1
    return created


def disband_class(n):
    """Create dictionary with 'n' keys+values whose in 'school' dictionary (to remove)"""
    i = 1
    disbanded = {}
    print(f"Let's disband {n} classes.\n")
    while i <= n:
        is_disbanded = input(f'Enter the number of {i} class: ')
        while is_disbanded not in school:
            is_disbanded = input(f'There is no class {is_disbanded} in this school.\n'
                                 f'Enter the number of {i} class: ')
            while is_disbanded in disbanded:
                is_disbanded = input(f'You are already select {is_disbanded} class.\n'
                                     f'Enter the number of {i} class: ')
        while is_disbanded in disbanded:
            is_disbanded = input(f'You are already select {is_disbanded} class.\n'
                                 f'Enter the number of {i} class: ')
            while is_disbanded not in school:
                is_disbanded = input(f'There is no class {is_disbanded} in this school.\n'
                                     f'Enter the number of {i} class: ')
        disbanded[is_disbanded] = "null"
        i += 1
    return disbanded


school = {'1a': '25', '1b': '23', '1c': '20', '2a': '21', '2b': '22', '2c': '26'}
show_school()
while True:
    # Get user's input
    usr_select = input(f'what do you want to do?\n'
                       f'1 - Change the number of pupils in classes.\n'
                       f'2 - Create new classes.\n'
                       f'3 - Disband classes.\n')
    if usr_select == 'exit':
        break
    else:
        # Check user input is a number and select function to run
        try:
            usr_choice = int(usr_select)
            if not 0 < usr_choice < 4:
                print(f'There is no variant with number {usr_choice}')
            else:
                usr_func(usr_choice)
        except ValueError:
            print("This is not a number. ")
        finally:
            print("Type 'exit' to quit, or choose, ", end='')

