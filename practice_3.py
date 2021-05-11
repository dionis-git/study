# Check if a number is positive, negative, or NULL.
while True:
    user_input = (input('enter a number:\n'))
    if user_input == 'exit':
        break
    else:
        # Check user input can get converted to 'float'
        try:
            user_variable = float(user_input)
            # Check the sign of the number
            if user_variable > 0:
                print("This is a positive number.")
            elif user_variable < 0:
                print("This is a negative number.")
            else:
                print('This is a NULL')
        except ValueError:
            print("This is not a number. ")
        finally:
            print("Type 'exit' to quit, or ", end='')
