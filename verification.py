def task1():
    print('Task 1')
    try:
        x = int(input(f'Enter any number from 1 to 9: '))
        if not 0 < x < 10:
            print(f'Input error')
        elif x > 6:
            for i in range(10):
                x += 1
                print(x)
        elif x > 3:
            m = float(input(f'Enter the degree to which the number should be raised: '))
            print(f'{x ** m}')
        else:
            s = input(f'Enter any string: ')
            n = int(input('Enter a number of string repeats: '))
            for i in range(n):
                print(s)
    except ValueError:
        print(f'Input error')
    print('\n')


def task2():
    print('Task 2')
    print('"Society at the beginning of the XXI century"')
    while True:
        try:
            age = int(input(f'How old are you? '))
            if not 0 <= age <= 120:
                for i in range(5):
                    print('Error! This is a program for people!')
            elif age >= 60:
                print('You are given a choice')
            elif age >= 25:
                print('You need to go to work')
            elif age >= 18:
                print('You need to go to a professional education institution')
            elif age >= 7:
                print('You need to go to school')
            else:
                print('You need to go to kindergarten')
            break
        except ValueError:
            print('Enter your age please.')
    print('\n')


while True:
    user_choice = input(f'choose task 1 or 2: ')
    if user_choice == 'exit':
        break
    try:
        user_choice = int(user_choice)
        if not 0 < user_choice < 3:
            print(f'There is no task with number {user_choice}.')
        elif user_choice == 1:
            task1()
        elif user_choice == 2:
            task2()
        else:
            print(f'There is no task with number {user_choice}.')
    except ValueError:
        print(f'This is not a number. ')
    finally:
        print('Enter "exit" to quit, or ', end='')
