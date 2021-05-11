def func1(num):
    n = num * 5
    print(n)


def func(n):
    if n < 3:
        n *= 10
        return n


k = 10

print(f'func1(num) = num * 5, global variable {k = }\nfor k func1(k):')
func1(k)
print('for number "-5" func1(-5):')
func1(-5)
print('for string "ab" func1("ab"):')
func1("ab")
print('\n')

a = 2
b = func(a)
print(f'func(n) = n * 10, if n < 3\n'
      f'for a = 2 and b = func(a):\n'
      f'the "b" variable will only be defined if the "func(a)" function returns a value to "main":\n'
      f'{b = }\n')
