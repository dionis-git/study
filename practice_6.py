def load_data():
    """Creates a questionnaire based on the user's gender"""
    while True:
        gender = input("Hi! Are you a man or a woman?\n")
        if gender == "Man" or gender == "man":
            gender = "male"
            break
        elif gender == "Woman" or gender == "woman":
            gender = 'female'
            break
    name = input("What's your name?\n")
    age = input("How old are you?\n")
    place = input("Where are you live?\n")
    print('\n')
    if gender == "male":
        print(f'This is {name}.\n'
              f'He is {age}.\n'
              f'He lives in {place}.\n')
    elif gender == "female":
        print(f'This is {name}.\n'
              f'She is {age}.\n'
              f'She lives in {place}.\n')


def load_example():
    """Prompts the user to solve the example"""
    solved = False
    while not solved:
        solve = input('Try to solve an example: 4*100-54 = ')
        if solve == str(4 * 100 - 54):
            solved = True
            print('This is the right decision. Congratulations!\n')
        else:
            print('This is the wrong decision, please try again.')


while True:
    # Get user's input
    u_select: str = (input('enter the job number:\n'
                           '1 - data.py\n'
                           '2 - example.py\n')
                     )
    if u_select == 'exit':
        break
    else:
        # Check user input is a number and load an example
        try:
            choice = int(u_select)
            if choice == 1:
                load_data()
            elif choice == 2:
                load_example()
            else:
                print(f'There is no job with number {choice}.')
        except ValueError:
            print("This is not a number.")
        finally:
            print("Type 'exit' to quit, or ", end='')
