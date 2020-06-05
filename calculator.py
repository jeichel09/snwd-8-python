a = int(input('First number: '))
b = int(input('Second number: '))

operation = input('What operation ("+, -, *, /") do you want? : ')

if operation == '+':
    print(a+b)
elif operation == '-':
    print(a-b)
elif operation == '*':
    print(a*b)
elif operation == '/':
    print(a/b)
else:
    print('This is an unknown operation')