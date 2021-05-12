import sys


def import_practice():
    """Import or reload the module of practice work"""
    practice = 'practice_' + u_input
    if practice in sys.modules:
        del sys.modules[practice]
    print(f"Practice {u_input}\n"
          f"----------")
    __import__(practice)


print('Python homework by Denis Sklyarov, group 1-76, ', end='')
while True:
    # Get the user's input
    u_input: str = (input('enter the number of Practice:\n'
                          '1 - Data types\n'
                          '2 - Boolean expressions\n'
                          '3 - Condition "if"\n'
                          '4 - Multiple conditions\n'
                          '5 - "while" loop\n'
                          '6 - "input()" method\n'
                          '7 - Strings as sequences\n'
                          '8 - List as changeable sequences\n'
                          '9 - Dictionaries\n'
                          '10 - "for" loop\n'
                          '11 - Functions\n'
                          '12 - Local and global variables\n'
                          '13 - Verification work\n')
                    )
    if u_input == 'exit':
        break
    else:
        # Check user's input is a number and import Practice
        try:
            u_choice = int(u_input)
            if not 0 < u_choice < 14:
                print(f'There is no Practice with number {u_choice}')
            elif u_choice == 13:
                if 'verification' in sys.modules:
                    del sys.modules['verification']
                print(f"Verification work\n"
                      f"-----------------")
                __import__('verification')
            else:
                import_practice()
        except ValueError:
            print("This is not a number. ")
        finally:
            print("\nType 'exit' to quit, or ", end='')
print('\nSee you!')
