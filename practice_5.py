a = 0
b = 1
print('The first twelve of the Fibonacci Sequence:')
print(a, b, end=' ')
n = 10
i = 0
while i < n:
    fib_sum = a + b
    print(fib_sum, end=' ')
    a, b = b, fib_sum
    i += 1
print('\n')

a = 3
b = 5
print('The list of the Fibonacci Sequence from 5-th to 20-th:')
print(a, b, end=' ')
n = 13
i = 0
while i <= n:
    fib_sum = a + b
    print(fib_sum, end=' ')
    a, b = b, fib_sum
    i += 1
print('\n')

# Interactive Fibonacci Sequence generate

while True:
    start = input("Enter the first term of the Fibonacci Sequence:\n")
    if start.isdigit():
        int_start = int(start)
        break

while True:
    stop = input("Enter the last term of Fibonacci Sequence:\n")
    if stop.isdigit():
        int_stop = int(stop)
        if int_stop >= int_start:
            break
        else:
            print('The last term must be equal or bigger than the first one!')
fib = []
a, b, i, n = 0, 1, 1, int_stop - 2
fib.extend([a, b])
while i <= n:
    fib_sum = a + b
    fib.append(fib_sum)
    a, b = b, fib_sum
    i += 1

fib_interactive = fib[int_start - 1:int_stop]
print(f'The Fibonacci Sequence from {int_start}-th to {int_stop}-th terms is:')
for i in fib_interactive:
    if i % 20 == 0:
        print('\n')
    print(i, end=' ')
print('\n')
