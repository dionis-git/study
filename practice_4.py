# Check the first number
while True:
    var1 = (input('enter first number:\n'))
    if var1 == 'exit':
        break
    else:
        # Check user input can get converted to 'float'
        try:
            float_var1 = float(var1)
            # Check the second number
            while True:
                var2 = (input('enter second number:\n'))
                if var2 == 'exit':
                    break
                else:
                    # Check user input can get converted to 'float'
                    try:
                        float_var2 = float(var2)
                        break
                    except ValueError:
                        print("This is not a number. Type 'exit' to quit, or ", end='')
            break
        except ValueError:
            print("This is not a number. Type 'exit' to quit, or ", end='')


# Calculate the result
def user_exit():
    """Compares the entered numbers and prints the greater one"""
    if var1 == 'exit' or var2 == 'exit':
        return ()
    if float_var1 > float_var2:
        result = float_var1 - float_var2
    elif float_var2 > float_var1:
        result = float_var1 + float_var2
    else:
        result = float_var1

    print(f'{result = }\n')


user_exit()
