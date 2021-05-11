# Create variables
var_int = 10
var_float = 8.4
var_str = "No"

print(f'{var_int = }, {var_float = }, {var_str = }\n')

# Modify and link variables

print(f'big_int = {var_int * 3.5 = }\n')
big_int = var_int * 3.5  # But really this is not 'int' but 'float'. Actually modify big_int = int(big_int).

print(f'var_float = {var_float - 1 = }\n')
var_float -= 1

print(f"{var_int / var_float = }\n{big_int / var_float = }\n")

print(f'var_str = {var_str * 2 + "Yes" * 3 = }\n')
var_str = var_str * 2 + "Yes" * 3

# Print variables
print(f"{var_int = }\n"
      f"{var_float = }\n"
      f"{var_str = }\n"
      f"{big_int = }\n"
      )
