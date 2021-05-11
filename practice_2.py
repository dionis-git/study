# Create variables
int1, int2 = 4, 16
str1, str2, str3, str4 = ['eniky', 'beniky', 'eli', 'vareniky']

# Complex boolean expressions with integers
print(f"{int1 = }\n{int2 = }\n")

print('Complex boolean expressions with "and":\n'
      f"{int1 < int2 and int1 != 0 = }\n"
      f"{int1 == int2 / 4 and int1 == int2 ** 0.5 = }\n"
      f"{int1 == int2 ** 2 and int2 < int1 = }\n"
      f"{int2 < 0 and int1 != 4 = }\n"
      )

print('Complex boolean expressions with "or":\n'
      f"{int1 < int2 or int1 == 0 = }\n"
      f"{int2 != int1 ** 2 or int1 == int2 ** 0.5 = }\n"
      f"{int1 == int2 ** 2 or int2 <= int1 = }\n"
      f"{int2 < 0 or int1 != 4 = }\n"
      )

# Complex boolean expressions with strings
print(f"{str1 = }\n"
      f"{str2 = }\n"
      f"{str3 = }\n"
      f"{str4 = }\n"
      )

print('Complex boolean expressions with "and":\n'
      f"{len(str1 + str2) == 11 and len(str1 * 2) != 11 = }\n"
      f"{str2 == 'b' + str1 and str2 < str1 = }\n"
      f"{len(str2) < 0 and str1 != str4 = }\n"
      f"{str1 < str2 and str1 != 0 = }\n"
      )

print('Complex boolean expressions with "or":\n'
      f"{str2 == str1 * 2 or str4 == 'var' + str1 = }\n"
      f"{str1 == str3 or str2 <= str1 = }\n"
      f"{str3 * 2 > str4 or str2 != 'b' + str1 = }\n"
      f"{str1 < str2 or len(str1) == 0 = }\n"
      )
