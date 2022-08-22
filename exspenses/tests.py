from django.test import TestCase

# Create your tests here.

x = float(input('Введите число:'))
s = input("Знак(+,-,*,/):")
y = float(input('Введите число:'))

if s == "+":
    print(x+y)
elif s == "-":
    print(x-y)
elif s == "*":
    print(x*y)
elif s == "/":
    if y != 0:
        print(x / y)
    else:
        print('Деление на ноль')

else:
    print('Введен не правильный знак')






