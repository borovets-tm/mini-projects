def repeat(name, count):
    repeat = input(f'{name}, ты хочешь спросить меня о чем-то еще? \n Д/Y - да, Н/N - нет\n').lower()
    if repeat == 'д' or repeat == 'l' or repeat == 'y':
        count += 1
        welcome_user(name, count)
    else:
        print('Возвращайся если возникнут вопросы!')
        
def answer_magic_ball(name_user, count):
    from random import choice
    answers = ['бесспорно', 'мне кажется - да', 'пока неясно, попробуй снова', 'даже не думай', 'предрешено', 'вероятнее всего', 'спроси позже', 'мой ответ - нет', 'никаких сомнений', 'хорошие перспективы', 'лучше не рассказывать',	'по моим данным - нет', 'определённо да', 'знаки говорят - да', 'сейчас нельзя предсказать', 'перспективы не очень хорошие', 'можешь быть уверен в этом', 'да', 'сконцентрируйся и спроси опять', 'весьма сомнительно']
    print(f'{name_user.upper()}, {choice(answers).upper()}!')
    repeat(name_user, count)

def welcome_user(name, count):
    if count == 1:
        name = input(f'Дорогой друг, как тебя зовут? \n').title()
        question = input(f'Привет, {name}! \nЗадай мне свой вопрос!\n')
    else:
        question = input(f'{name}, задай свой следующий вопрос!\n')
    answer_magic_ball(name, count)

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name = ''
count = 1
welcome_user(name, count)