dir_ed = ['encrypt', 'decrypt']
rus = ['rus', 'кгы']
eng = ['eng']
letters_en = 25
letters_ru = 31

def is_valid(shift_step, language, let_er):
    if language in rus:
        message = f'Введите шаг сдвига  от 1 до 31 включительно\n'
    else:
        message = f'Enter the shift step from 1 to 24 inclusive\n'
    while shift_step.isdigit() == False or int(shift_step) > let_er or int(shift_step) < 0:
        shift_step = input(message)
    return int(shift_step)
    
def is_valid_lang(lang):
    while lang not in rus + eng:
        lang = input(f'Попробуйте снова. Try again.\nВыберите Ваш разговорный язык\nChoose your language\nrus - русский, eng - english\n').lower()
    return lang

def repeat(lang):
    repeat = input(f'Ты решил чего хочешь? Have you decided what you want?\n Д/Y - да, Н/N - нет\n').lower()
    if (lang in rus and repeat in 'дl') or (lang in eng and repeat == 'y'):
        welcome_user()
    else:
        print('Тогда прощай! Then goodbye!')

def welcome_user():
    language = is_valid_lang(input(f'Выберите Ваш разговорный язык\nChoose your language\nrus - русский, eng - english\n').lower())
    if language in rus:
        direction = ('encrypt' if input(f'Зашифровать сообщение?\nД - да, Н - нет\n').lower() in 'дl' else '')
        if direction == '':
            direction = ('decrypt' if input(f'Раcшифровать сообщение?\nД - да, Н - нет\n').lower() in 'lд' else print('Возвращайтесь, когда определитесь, что Вам нужно'))
        if direction in dir_ed:
            shift_steps(language, direction)
        else:
            repeat(language)
    if language in eng:
        direction = ('encrypt' if input(f'Encrypt the message?\nY - yes, N - no\n').lower() == 'y' else '')
        if direction == '':
            direction = ('decrypt' if input(f'Decrypt the message?\nY - yes, N - no\n').lower() == 'y' else print('Come back when you decide what you need'))
        if direction in dir_ed:
            shift_steps(language, direction)
        else:
            repeat(language)
            
def shift_steps(language, direction):
    if language in rus:
        shift_step = input(f'Укажите шаг сдвига алфавита\n')
        let_er = letters_ru
    else:
        shift_step = input(f'Specify the alphabet shift step\n')
        let_er = letters_en
    shift_step = is_valid(shift_step, language, let_er)
    cipher_language(language, shift_step, direction)    

def cipher_language(language, shift_step, direction):
    lowercase_letters_en = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    uppercase_letters_en = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase_letters_ru = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    uppercase_letters_ru = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
    txt = []
    if language in rus:
        txt.extend(input(f'Введите текст для шифровки или рашифровки\n'))
        caesar_cipher(shift_step, txt, lowercase_letters_ru, uppercase_letters_ru, letters_ru, direction, language)
    else:
        txt.extend(input(f'Enter the text to encrypt or decrypt\n'))
        caesar_cipher(shift_step, txt, lowercase_letters_en, uppercase_letters_en, letters_en, direction, language)

def caesar_cipher(shift_step, txt, lowercase_letters, uppercase_letters, letters, direction, lang):
    for i in range(len(txt)):
        if txt[i] in lowercase_letters:
            let_s = lowercase_letters
        elif txt[i] in uppercase_letters:
            let_s = uppercase_letters
        else:
            continue
        s = let_s.index(txt[i])
        if direction == dir_ed[1]:  #decrypt
            x = s - shift_step
            y = x + letters + 1
        else:                       #encrypt
            x = s + shift_step
            y = x - letters - 1
        if -1 < x <= letters:
            txt[i] = let_s[x]
        else:
            txt[i] = let_s[y]
    print(''.join(txt))
    verification(lang, direction)
      
def verification(language, direction):
    verification = input(f'Все верно? Is that right? \nД/Y - да/yes, Н/N - нет, no\n').lower()
    if verification in 'lд' and language in rus:
        print('Рад, что все получилось! Удачи')
    elif verification == 'y' and language in eng:
        print("I'm glad that everything worked out! Good luck")
    else:
        shift_steps(language, direction)
        
welcome_user()