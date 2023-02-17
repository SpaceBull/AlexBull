def code():
    print('\n    ГЛАВНОЕ МЕНЮ')
    print('\nВыберите действие:')
    print('1. Зашифровать сообщение')
    print('2. Расшифровать сообщение')

    action = int(input('\nВведите номер действия: '))

    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    alphabet = list(alphabet)
    new_text = []

    text = input('\nВведите сообщение: ').lower()
    shift = int(input('Введите сдвиг: '))
    for symbol in text:
        if symbol not in list(alphabet):
            new_text.append(symbol)
            continue
        index = alphabet.index(symbol)
        if action == 1:
            index_symbol = index + shift
            if index_symbol >= 32:
                index_symbol = (index_symbol % 32) - 1
                new_symbol = alphabet[index_symbol]
                new_text.append(new_symbol)
            else:
                new_symbol = alphabet[index_symbol]
                new_text.append(new_symbol)
        if action == 2:
            index_symbol = index - shift
            if index_symbol >= 32:
                index_symbol = 32 - index_symbol + 1
                new_symbol = alphabet[index_symbol]
                new_text.append(new_symbol)
            else:
                new_symbol = alphabet[index_symbol]
                new_text.append(new_symbol)
    result = ''.join(new_text)
    print(f'Ответ: {result}')
    menu = input('Нажми любую букву для выхода в меню: ')
    if menu:
        code()


code()
