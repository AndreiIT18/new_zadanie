name = input('Введите имя: ')
name2 = input('Введите фамилию: ')
print(name, name2)

a = int(input('Введите число A: '))
b = int(input('Введите число B: '))
c = a*b
print(c)

name1 = int(input('Введите число: ')) 
if name1 > 0:
    name1 = 'andrei'
    print(name1)
elif name1 < 0:
    name1 = 'anna'
    print(name1)

number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))
for el in range(10):
    if el > 0:
        number1 = True
        print(number1)
    elif el < 0 :
        number1 = False
        print(number1)
    
chis1 = int(input('введите число'))
print('Я загодал число! Угодай его!')
chis1 = int(input('Введите число: '))

if chis1 != 2:
    chis1 = 'Неверно!'
    print(chis1)
elif chis1 == 2 :
    chis1 = 'Угодал, это число 2'
    print(chis1)
