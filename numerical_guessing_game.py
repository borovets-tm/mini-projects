def is_valid(user_num, max_n):
    while not user_num.isdigit() or int(user_num) > max_n or int(user_num) < 1:
        user_num = input(f'А может быть все-таки введем целое число от 1 до {max_n}? ')
    return int(user_num)


def repeat(count):
    if count == 1:
        word_used = 'попытку'
    elif 1 < count < 6:
        word_used = 'попытки'
    else:
        word_used = 'попыток'
    print(f'{name.title()} угадал число за {count} {word_used}')
    check = input('Сыграем еще? \nД/Y - да, Н/N - нет\n').lower()
    if check == 'д' or check == 'l' or check == 'y':
        welcome_user(name)
    else:
        print('Спасибо, что играли в числовую "Угадайку". Еще увидимся...')


def welcome_user(user):
    from random import randint
    print(f'Добро пожаловать в в числовую "Угадайку" {user.title()}!')
    right = input('Укажи максимальное число для отгадки... ')
    while not right.isdigit():
        right = input('Укажи максимальное число для отгадки... ')
    right = int(right)
    s_num = randint(1, right)
    num = input(f'Введи число от 1 до {right} ')
    num = is_valid(num, right)
    numerical_guessing_game(num, s_num, right)
    return name.title()


def numerical_guessing_game(answer, number, max_n):
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
