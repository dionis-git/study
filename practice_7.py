text = input("Enter the text:\n")
while len(text) < 8:
    text = input("Enter at least 8 characters:\n")
print(f'Your string is "{text}".\n'
      f'In this string:\n'
      f'the first character is "{text[0]}"\n'
      f'the last character is "{text[-1]}"\n'
      f'the third character is "{text[2]}"\n'
      f'the third character from the end is "{text[-3]}"\n'
      f'the first eight characters are "{text[:8]}"\n'
      f'the four characters from the middle are "{text[(len(text) // 2 - 2): (len(text) // 2 + 2)]}"\n'
      f'the characters with indexes that are multiples of three are "{text[3::3]}"')
