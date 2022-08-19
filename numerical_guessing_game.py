def is_valid(user_num, max_n):
    while user_num.isdigit() == False or int(user_num) > max_n or int(user_num) < 1:
        user_num = input(f'А может быть все-таки введем целое число от 1 до {max_n}? ')
    return int(user_num)

def repeat(count):
    if count == 1:
        popyt = 'попытку'
    elif 1 < count < 6:
        popyt = 'попытки'
    else:
        popyt = 'попыток'
        print(f'{name.title()} угадал число за {count} {popyt}')
    repeat = input('Сыграем еще? \nД/Y - да, Н/N - нет\n').lower()
    if repeat == 'д' or repeat == 'l' or repeat == 'y':
        welcome_user(name)
    else:
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')

def welcome_user(name):
    from random import randint
    print(f'Добро пожаловать в в числовую угадайку {name.title()}!')
    right = input('Укажи максимальное число для отгадки... ')
    while right.isdigit() == False:
        right = input('Укажи максимальное число для отгадки... ')
    right = int(right)
    s_num = randint(1, right)
    num = input(f'Введи число от 1 до {right} ')
    num = is_valid(num, right)
    count = ugadaika(num, s_num, right)
    return name.title()

def ugadaika(answer, number, max_n):
    count = 1
    while answer != number:
        if answer < number:
            answer = is_valid(input('Ваше число меньше загаданного, попробуйте еще разок '), max_n)
            count += 1
        elif answer > number:
            answer = is_valid(input('Ваше число больше загаданного, попробуйте еще разок '), max_n)
            count += 1
    print('Вы угадали, поздравляем!')
    repeat(count)

name = input('Как Вас зовут? ')
name = welcome_user(name)