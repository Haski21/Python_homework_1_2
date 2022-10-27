'''
Задача №3
Дано натуральное число N. Если число N двузначное,
то найти сумму цифр числа. Если число N трехзначное,
то найти произведение ненулевых цифр числа
иначе написать, что число неподходящее
'''

number = int(input('Write number: '))

if number > 9 and number <100:
    print('sum of 2-x number is:', int(number / 10) + number % 10)
elif number > 99 and number < 1000:
    #пока писал, задумался, а что насчет видимости переменных в других функциях?
    number_one = int(number / 100)
    number_two = int((number % 100/10))
    number_three = int(number % 10)
    #по факту не нужно делать проверку первой цифры, тк если ввести 023,то примет за 2-х знвчное?
    if number_two:
        if number_three:
            print('multiplication is:', number_one * number_two * number_three)
        else: print('multiplication is:', number_one * number_two)
    elif number_three:
        print('multiplication is:', number_one * number_three)
    else: print('multiplication is:', number_one)
else: print('number is bad(')
