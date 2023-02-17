SEPARATOR = '------------------------------------------'

# user profile
name_person = ''
age = 0
number_phone = ''
index_person = ''
postal_address = ''
email = ''
info = ''
# social links
result_ogrnip = 0
inn = 0
result_payment_account = 0
name_bank = ''
bik = 0
correspondent_account = 0


def general_info_user(name_parameter, age_parameter,
                      number_phone_parameter, email_parameter,
                      index_parameter,
                      postal_parameter, info_parameter):
    print(SEPARATOR)
    print('Имя:    ', name_parameter)
    if 11 <= age_parameter % 100 <= 19:
        years_parameter = 'лет'
    elif age_parameter % 10 == 1:
        years_parameter = 'год'
    elif 2 <= age_parameter % 10 <= 4:
        years_parameter = 'года'
    else:
        years_parameter = 'лет'

    print('Возраст:', age_parameter, years_parameter)
    print('Телефон:', number_phone_parameter)
    print('E-mail: ', email_parameter)
    print('Индекс: ', index_parameter)
    print('Адрес: ', postal_parameter)
    if info:
        print('')
        print('Дополнительная информация:')
        print(info_parameter)


print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
    print(SEPARATOR)
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')

    option = int(input('Введите номер пункта меню: '))
    if option == 0:
        break

    if option == 1:
        while True:
            print(SEPARATOR)
            print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Информация о предпринимателе')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                name_person = input('Введите имя: ')
                while 1:
                    age = int(input('Введите возраст: '))
                    if age > 0:
                        break
                    print('Возраст должен быть положительным')

                enter_number_phone = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
                number_phone = ''
                for symbol_number in enter_number_phone:
                    if symbol_number == '+' or ('0' <= symbol_number <= '9'):
                        number_phone += symbol_number

                email = input('Введите адрес электронной почты: ')
                index_person = ''
                index = input('Введите индекс: ')
                for symbol in list(index):
                    if symbol.isdigit():
                        index_person += symbol
                postal_address = input('Введите почтовый адрес (без индекса): ')
                info = input('Введите дополнительную информацию:\n')

            elif option2 == 2:
                flag = False
                while not flag:
                    ogrnip = input('Введите ОГРНИП: ')
                    for elem in list(ogrnip):
                        if elem.isalpha():
                            print('Введите ОГРНИП без букв!')
                            break
                    else:
                        if len(ogrnip) == 15:
                            result_ogrnip = int(ogrnip)
                            flag = True
                        else:
                            print('ОГРНИП должен содержать 15 цифр')
                inn = int(input('Введите ИНН: '))
                flag_2 = False
                while not flag_2:
                    payment_account = input('Введите расчётный счёт: ')
                    for elem in list(payment_account):
                        if elem.isalpha():
                            print('Введите расчётный счёт без букв!')
                            break
                    else:
                        if len(payment_account) == 20:
                            result_payment_account = int(payment_account)
                            flag_2 = True
                        else:
                            print('расчётный счёт должен содержать 20 цифр')
                name_bank = input('Название банка: ')
                bik = int(input('Введите БИК: '))
                correspondent_account = int(input('Введите корреспондентский счёт: '))
            else:
                print('Введите корректный пункт меню')

    elif option == 2:
        while True:
            print(SEPARATOR)
            print('ВЫВЕСТИ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Вся информация')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                general_info_user(name_person, age, number_phone, email, index_person, postal_address, info)

            elif option2 == 2:
                general_info_user(name_person, age, number_phone, email, index_person, postal_address, info)
                print('')
                print('Информация о предпринимателе')
                print('ОГРНИП:', result_ogrnip)
                print('ИНН: ', inn)
                print('Банковские реквизиты')
                print('Р/с:   ', result_payment_account)
                print('Банк: ', name_bank)
                print('БИК: ', bik)
                print('К/с: ', correspondent_account)
            else:
                print('Введите корректный пункт меню')
    else:
        print('Введите корректный пункт меню')