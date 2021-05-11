def load_sum():
    count = input(f"Let's calculate the sum of any numbers,\n"
                  f"how many numbers do you want to sum? ")
    while not count.isdigit():
        if count == 'exit':
            break
        count = input(f"Enter 'exit' to quit or select how many numbers do you want to sum? ")
    if count.isdigit():
        print(f'The sum is {usr_sum(int(count))}')


def load_max():
    count = input(f"Let's calculate the maximum of any numbers,\n"
                  f"how many numbers do you want to compare? ")
    while not count.isdigit():
        if count == 'exit':
            break
        count = input(f"Enter 'exit' to quit or select how many numbers do you want to compare? ")
    if count.isdigit():
        print(f'The maximum is {usr_max(int(count))}')


def usr_sum(n):
    i = 1
    var_list = []
    while i <= n:
        var = (input(f'enter {i} number:\n'))
        if var == 'exit':
            break
        else:
            # Check user input can get converted to 'float' and add it to list
            try:
                var_list.append(float(var))
                i += 1
            except ValueError:
                print("This is not a number. Type 'exit' to quit, or ", end='')
    return sum(var_list)


def usr_max(n):
    i = 1
    var_list = []
    while i <= n:
        var = (input(f'enter {i} number:\n'))
        if var == 'exit':
            break
        else:
            # Check user input can get converted to 'float' and add it to list
            try:
                var_list.append(float(var))
                i += 1
            except ValueError:
                print("This is not a number. Type 'exit' to quit, or ", end='')
    return max(var_list)


while True:
    # Get user's input
    u_select: str = (input('enter the function number:\n'
                           '1 - calculate the sum of any numbers\n'
                           '2 - calculate the maximum of any numbers\n')
                     )
    if u_select == 'exit':
        break
    else:
        # Check user input is a number and load the function
        try:
            choice = int(u_select)
            if choice == 1:
                load_sum()
            elif choice == 2:
                load_max()
            else:
                print(f'There is no job with number {choice}.')
        except ValueError:
            print("This is not a number.")
        finally:
            print(f"\nType 'exit' to quit, or ", end='')


