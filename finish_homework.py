#17.1

left_lin = int(input('Левая граница: '))
right_lin = int(input('Правая граница: '))

answer_cub = [x ** 3 for x in range(left_lin, right_lin + 1)]
print(f'Список кубов чисел в диапазоне от {left_lin} до {right_lin}: {answer_cub}')

answer_square = [x ** 2 for x in range(left_lin, right_lin + 1)]
print(f'Список квадратов чисел в диапазоне от {left_lin} до {right_lin}: {answer_square}')
####################################################################################
#17.2
text = input('Введите строку: ')
symbol = input('Введите дополнительный символ: ')

roster_double = [sym * 2 for sym in text]
print(f'Список удвоенных символов: {roster_double}')

roster_word_symbol = [sym * 2 + symbol for sym in text]
print(f'Склейка с дополнительным символом: {roster_word_symbol}')

####################################################################################
def considers_price_increases(precent, iteration):
    return round(iteration * (1 + precent / 100), 2)

price = [1.09, 23.56, 57.84, 4.56, 6.78]
first_precent = int(input('Повышение на первый год: '))
second_precent = int(input('Повышение на второй год: '))

first_sum = [considers_price_increases(first_precent, i_price) for i_price in price]
second_sum = [considers_price_increases(second_precent, i_price) for i_price in first_sum]

print(f'Сумма цен за каждый год: '
      f'{round(sum(price), 2)}, {round(sum(first_sum), 2)}, {round(sum(second_sum), 2)}')
####################################################################################
import random

original_prices = [random.randint(-2, 5) for i in range(5)]
new_prices = original_prices[:]

for i in range(len(original_prices)):
    if new_prices[i] < 0:
        new_prices[i] = 0

print("Мы потеряли: ",  sum(original_prices) - sum(new_prices))
print(new_prices)
############################################################################
nums = [48, -10, 9, 38, 17, 50, -5, 43, 46, 12]

print(nums[:5]) # первые пять элементов списка.
print(nums[:-2]) # весь список, кроме последних двух элементов
print(nums[::2]) # все элементы с чётными индексами
print(nums[1::2]) # все элементы с нечётными индексами
print(nums[::-1]) # выведите все элементы в обратном порядке
print(nums[::-2]) #все элементы списка через один в обратном порядке, начиная с последнего.
###########################################################################
import random

number = int(input('Введите количество чисел N: '))
numbers = [random.randint(-10, 10) for i in range(number)]
print(numbers)
a = random.randint(0, len(numbers) - 1)
b = random.randint(a, len(numbers) - 1)

print(a, b)
answer = numbers[:a] + numbers[b + 1:]
#price = numbers[a:b + 1]
print(answer)
###########################################################################
name = input('Имя:')
order_number = int(input('Номер заказа: '))

print('Здравствуйте, {name_percona}! Ваш номер заказа: {order}. '
      'Приятного дня!'.format(name_percona=name,
                              order=order_number))
###########################################################################
name = input('Имя:')
order_number = int(input('Номер заказа: '))

print('Здравствуйте, {0}! Ваш номер заказа: {1}. Приятного дня!'.format(name, order_number))
###########################################################################
ip_address = "Айпи {0}.{1}.{2}.{3}"
count = 0
numbers = []
while count < 4:
    new_number = int(input("Введите число: "))
    numbers.append(new_number)
    if 0 <= new_number <= 255:
        count += 1

print(ip_address.format(*numbers))
# * полезный инструмент, но и без него можно справиться, вручную прописав элементы по индексам
print(ip_address.format(numbers[0], numbers[1], numbers[2], numbers[3]))
#############################################################################
import random
number = int(input('Количество чисел в списке:  '))
roster_numbers = [random.randint(0, 2) for _ in range(number)]
print(f'Список до сжатия: {roster_numbers}')

num_one = [num for num in roster_numbers if num > 0]
print(f'Список после сжатия: {num_one}')
##############################################################################
import random

command_1 = [random.randint(50, 80) for _ in range(10)]
command_2 = [random.randint(30, 60) for _ in range(10)]
command_3 = ['Погиб' if command_1[index] + command_2[index] > 100
             else 'Выжил' for index in range(10)]

print(f'Урон первого отряда: {command_1}')
print(f'Урон второго отряда: {command_2}')
print(f'Состояние третьего отряда: {command_3}')
###############################################################################
original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]

answer = [i if i > 0 else 0 for i in original_prices]
print(answer)
###############################################################################
import random

number = int(input('Введите количество чисел N: '))
numbers = [random.randint(-10, 10) for i in range(number)]
print(numbers)
a = random.randint(0, len(numbers) - 1)
b = random.randint(a, len(numbers) - 1)

print(a, b)
answer = numbers[:a] + numbers[b + 1:]
#price = numbers[a:b + 1]
print(answer)
##############################################
text = input('Введите текст: ').split()
text = ' '.join(text)
print(text)
##########################################
word = ['дорога', 'горы', 'трава']  #[input("Введите слово: ") for _ in range(3)]
text = input('Введите текст: ')
number_word = [text.count(i_text) for i_text in word]
print(number_word)
####################################################

while True:
    pattern = input('Введите шаблон поздравления, в шаблоне можно использовать конструкцию {name} и {age}: ')
    if '{name}' and '{age}' in pattern:
        break
    print('Шаблон не содержит {name} и {age}')

names = input('Список людей через запятую: ').split(', ')
ages_str = input('Возраст людей через пробел: ').split()
ages = [int(age) for age in ages_str]

for i_man in range(len(names)):
    print(pattern.format(name=names[i_man], age=ages[i_man]))

result = [' '.join([names[i_man], str(ages[i_man])]) for i_man in range(len(names))]
answer = ', '.join(result)
print('Именинники:', answer)
###################################################################################################
#PK 18.1
menu = input('Доступное меню: ').split(';')
new_menu = ', '.join(menu)
print(f'На данный момент в меню есть: {new_menu}')
###################################################################################
#PK 18.2
word = input('Введите строку: ').split()
number_of_letters = 1
long_word = ''
for text in word:
    if number_of_letters <= len(text):
        number_of_letters = len(text)
        long_word = text

print(f'Самое длинное слово: {long_word}')
print(f'Длина этого слова: {len(long_word)}')
##################################################################################
#PK 18.3
name_file = input('Название файла: ')
bad_symbol = '@  №  $  %  ^  &  *  ( )'.split()
begin_word = True
for symbol in bad_symbol:
    if name_file.startswith(symbol):
        begin_word = False
        print('Ошибка: название начинается на один из специальных символов.')


if name_file.endswith('.txt') or name_file.endswith('.docx') and begin_word:
    print('Файл назван верно.')
else:
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
############################################################################################
# PK 18.4
text = input('Введите строку: ').split()
result = [word.title() for word in text]
result = ' '.join(result)
print(f'Результат: {result}')
#########################################################################################\
# PK 18.5
answer = False
while answer != True:
    password = input('Придумайте пароль: ')
    digits_in_the_password = len([number for number in password if number.isdigit()])
    if len(password) > 8 and password.islower() == False and digits_in_the_password >= 3:
        answer = True
        print('Это надёжный пароль!')
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
########################################################################################
# PK 18.6
text = input('Введите строку: ')
text = [letter for letter in text]
copy_text = text[:]
copy_text += '!'
index = -1
roster_letters = []
result_letters = []
answer = []
result = []

for letter in text:
    roster_letters.append(letter)
    index += 1
    if copy_text[index] != copy_text[index + 1]:
        result_letters.append(roster_letters)
        roster_letters = []

for letter in result_letters:
    str_letter = letter[0]
    count_letter = str(len(letter))
    answer = str_letter + count_letter
    result += answer
    result = ''.join(result)

print(f'Закодированная строка: {result}')
##################################################################
#PK 18.7
ip_address = input('Введите IP: ')
dot = ip_address.count('.')
answer = False
if dot == 3:
    for number in ip_address.split('.'):
        if not number.isdigit():
            print(f'{number} — это не целое число.')
            break
        if int(number) > 255:
            print(f'{number} превышает 255.')
            break
        if int(number) < 0:
            print(f'{number} меньше 0.')
            break
        if number.isdigit():
            answer = True
else:
    print('Адрес — это четыре числа, разделённые точками.')

if answer:
    print('IP-адрес корректен.')
######################################################################
#PK 18.8
first_line = input('Первая строка: ')
second_line = input('Вторая строка: ')
count_letter = len(first_line)
shift = 0

first_roster = [letter for letter in first_line]
second_roster = [letter for letter in second_line]

while count_letter != 0:
    shift += 1
    letter = second_roster[len(second_roster) - 1]
    copy_letter = letter
    second_roster.remove(letter)
    second_roster.insert(0, copy_letter)
    count_letter -= 1
    if second_roster == first_roster:
        print(f'Первая строка получается из второй со сдвигом {shift}.')
        break
    if count_letter == 0:
        print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
################################################################################################
#pk 18.9
text = input('Сообщение: ').split()
new_text = []
for word in text:
    if not word.isalpha():
        symbol = word[len(word) - 1]
        copy_symbol = symbol
        temp_word = [letter for letter in word]
        temp_word.remove(symbol)
        temp_word = temp_word[::-1]
        temp_word.insert(len(word) - 1, copy_symbol)
        word = ''.join(temp_word)
        new_text.append(word)
    else:
        new_text.append(word[::-1])

answer = ' '.join(new_text)
print(f'Новое сообщение: {answer}')
############################################################
#pk 18.10
def shift_in_alphabet(shift_text, code_line):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = list(alphabet)
    new_text = []
    for symbol in code_line.lower():
        if symbol not in alphabet:
            new_text.append(symbol)
            continue
        index = alphabet.index(symbol)
        index_symbol = index - shift_text #(- на расшифровку, + на закодирование)
        if index_symbol >= 25:
            index_symbol -= 26
            new_symbol = alphabet[index_symbol]
            new_text.append(new_symbol)
        else:
            new_symbol = alphabet[index_symbol]
            new_text.append(new_symbol)
    return new_text


def line_shift(new_text):
    result = ''.join(new_text)
    word_shift = 3 #сдвиг в слове
    symbol = '/'
    answer = []
    f = False
    for word in result.split():
        for _ in range(word_shift):
            letter = word[len(word) - 1]
            copy_word = list(word)
            copy_word.pop(len(word) - 1)
            copy_word.insert(0, letter)
            word = ''.join(copy_word)
            if symbol in list(word):
                word = list(word)
                word.remove('/')
                word_shift += 1
                result = ' '.join(answer)
                f = True
        if f:
            word += '.'
            f = False
        answer.append(word)
    return result

text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/' \
       'jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/' \
       'dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/' \
       'ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/' \
       'svmf ipvhiBmu zqsbdujdbmju fbutc uz/' \
       'qvsj Fsspst tipvme wfsof qbtt foumz/' \
       'tjm omfttV mjdjumzfyq odfe/' \
       'tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/' \
       'hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/' \
       ' Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/' \
       'Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/' \
       'op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /' \
       'jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/' \
       ' bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'

shift = int(input('Введите сдвиг в алфавите: ')) #1 Вводим
new_roster = shift_in_alphabet(shift, text)
print(line_shift(new_roster))
##############################################################################
#19.1-2
student_str = input(
  'Введите информацию о студенте через пробел\n'
  '(имя, фамилия, город, место учёбы, оценки): '
)
student_info = student_str.split()
print(student_info)
student = dict()
print(student)
student['имя'] = student_info[0]
student['фамилия'] = student_info[1]
student['город'] = student_info[2]
student['место учёбы'] = student_info[3]
student['оценки'] = []
for i in student_info[4:]:
    student['оценки'].append(int(i))

for i in student:
    print(i, '-', student[i])
###################################################
num = int(input('Введите целое число: '))
result = {}
for i in range(1, num + 1):
    result[i] = i ** 2

#quantity[4] = 130 - если надо заменить ключ (4) и придать другое значение
print(result)
#################################################
#19.1-3
book = dict()
for iteration in range(5):
    print(f'Текущие контакты на телефоне:\n {book}')
    name = input('Введите имя: ')
    phone = int(input('Введите номер телефона: '))
    if name not in book:
        book[name] = phone
    else:
        print('Такое Имя уже есть')
        break
########################################################
#19.2-1
small_storage = {
    'гвозди': 5000,
    'шурупы': 3040,
    'саморезы': 2000
}

big_storage = {
    'доски': 1000,
    'балки': 150,
    'рейки': 600
}

big_storage.update(small_storage)
for i in range(3):
    goods = input('Какой товар хотите найти? ')
    print(big_storage.get(goods))
########################################################
#19.2-2
incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}

print(f'Общий доход за год составил {sum(incomes.values())} рублей')

min_sale = min(incomes.values())
answer = ''
for i in incomes:
    if incomes[i] == min_sale:
        answer = i

incomes.pop(answer)
print(f'Самый маленький доход у {answer}. Он составляет {min_sale} рублей')
print(f'Итоговый словарь: {incomes}')
#############################################################################
#19.2-3
text = input('Введите текст: ').lower()
result = dict()

for symbol in text:
    if symbol in result:
        result[symbol] += 1
    else:
        result[symbol] = 1

for i in sorted(result.keys()):
    print(f'{i} - {result[i]}')

print(f'Максимальная частота: {max(result.values())}')
#####################################################################
#19.3-1
family_member = {
    "name": "Jane",
    "surname": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "name": "Alice",
            "age": 6
        },
        {
            "name": "Bob",
            "age": 8
        }
    ]
}

print(family_member["name"], family_member["surname"],
     family_member["hobbies"], family_member["age"],
     family_member["children"])

# for i in family_member["children"]: #Поиск боба по циклу
#     if i['name'] == 'Bob':
#       print(True)

#kind = [i['name'] for i in family_member["children"] if i['name'] == 'Bob']
#print(kind) #Поиск боба по циклу LC

result = {}
answer = dict()
for child in family_member["children"]: # Добавляем всех детей из списка
    result[child['name']] = child['age'] # чилдрена(значения)

if result.get('Bob'):
    print('Bob есть')
else:
    print('Bob-a нет')

childrens_surname = family_member.get("surname", None)
if childrens_surname:
    print(childrens_surname)
else:
    print("Nosurname")
#############################################################################
#19.3-2
players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}

rest = [player['name'] for player in players_dict.values()
        if player['team'] == 'A' and player['status'] == 'Rest']
print(f'члены команды из команды А, которые отдыхают {rest}')

training = [player['name'] for player in players_dict.values()
            if player['team'] == 'B' and player['status'] == 'Training']
print(f'члены команды из команды B, которые тренируются {training}')

travel = [player['name'] for player in players_dict.values()
          if player['team'] == 'C' and player['status'] == 'Travel']
print(f'члены команды из команды C, которые путешествуют {travel}')
############################################################################
#19.4-1
symbol = {'.', ',', ';', ':', '!', '?'}
text = input('Введите строку: ') #Я! Есть. Грут?! Я, Грут и Есть.
count = 0
for i in text:
    if symbol.intersection(i):
        count += 1

print(f'Количество знаков пунктуации: {count}')
############################################################################
#19.4-2
import random

nums_1 = [29, 17, 10, 15, 13, 22, 12, 22, 7, 24, 26, 3, 11, 2, 3, 16, 19, 21, 2, 3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1]
nums_2 = [16, 21, 30, 24, 5, 7, 23, 13, 11, 5, 21, 5, 19, 9, 12, 9, 15, 16, 29, 8, 16, 1, 22, 15, 16, 9, 1, 13, 21, 21]

dict_num_1 = set(nums_1)
dict_num_2 = set(nums_2)
print(f'1-е множество: {dict_num_1}')
print(f'2-е множество: {dict_num_2}')

print(f'Минимальный элемент 1-го множества: {min(dict_num_1)}')
dict_num_1.remove(min(dict_num_1))

print(f'Минимальный элемент 2-го множества: {min(dict_num_2)}')
dict_num_2.remove(min(dict_num_2))

random_number_1 = random.randint(100, 200)
dict_num_1.add(random_number_1)
print(f'Случайное число для 1-го множества: {random_number_1}')

random_number_2 = random.randint(100, 200)
dict_num_2.add(random_number_2)
print(f'Случайное число для 2-го множества: {random_number_2}')

print(f'Объединение множеств: {dict_num_1.union(dict_num_2)}')
print(f'Пересечение множеств: {dict_num_1.intersection(dict_num_2)}')
print(f'Элементы, входящие в nums_2, но не входящие в nums_1: {dict_num_2.difference(dict_num_1)}')
##########################################################################################################
#19.4-3
text = input('Введите строку: ') #Введите строку: ab1n32kz2
new_text = set(text) #- множество сразу сделала
result = set() # CОЗДАНИЕ ИМЕННО МНОЖЕСТВА! quantity = {} - словарь
for symbol in new_text:
    if '0' <= symbol <= '9': #  ЛАЙФХАК!!!!!!!!!!! в множестве  можно сравнивать строки!!!
        result.add(symbol)

print(f'Различные цифры строки: {result}')
############################################################################################################
#19PK-1
violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

number_text = {
    1: 'первой',
    2: 'второй',
    3: 'третьей',
    4: 'четвертой',
    5: 'пятой',
    6: 'шестой',
    7: 'седьмой'
}
answer = 0
number_of_songs = int(input('Сколько песен выбрать? '))
for number in range(1, number_of_songs + 1):
    song = input(f'Название {number_text[number]} песни: ')
    answer += violator_songs[song]

print(f'Общее время звучания песен: {answer} минуты')

############################################################################################################
#19.PK - 2
number_text = {
    0: 'Первая',
    1: 'Вторая',
    2: 'Третья',
    3: 'Четвертая',
    4: 'Пятая',
}
number_text_2 = {
    0: 'Первый',
    1: 'Второй',
    2: 'Третий',
}

roster_city = {}
number_of_countries = int(input('Количество стран: '))
for number in range(number_of_countries):
    country = input(f'{number_text[number]} страна: ').split()
    for city in country[1:]:
        roster_city[city] = country[0]

for number in range(3):
    search_city = input(f'{number_text_2[number]} город: ')
    country = roster_city.get(search_city)
    if country:
        print(f'Город {search_city} расположен в стране {country}.')
    else:
        print(f'По городу {search_city} данных нет.')

    ####Целый день изначально думал в таком подходе(

    # city = {}
    # number_of_countries = int(input('Количество стран: '))
    # for number in range(number_of_countries):
    #     country = input(f'{number_text[number]} страна: ').split(' ')
    #     city[country[0]] = country[1:]

    # for key_number, value in list(city.items()):
    #     if search_city in value:
    #         print(f'Город {search_city} расположен в стране {key_number}.')
    #         del city[key_number]

    #     else:
    #         print(f'По городу {search_city} данных нет.')

# Россия Москва Петербург Новгород
# Германия Берлин Лейпциг Мюнхен
#######################################################################
# pk 19.3
data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "totalIn": 444,
        "totalOut": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}
# Вывести списки ключей и значений словаря.
# В “ETH” добавить ключ “total_diff” со значением 100.
# Внутри “fst_token_info” значение ключа “name” поменять с “fdf” на “doge”.
# Удалить “total_out” из tokens и присвоить его значение в “total_out” внутри “ETH”.
# Внутри "sec_token_info" изменить название ключа “price” на “total_price”.

# 1
for key, value in data.items():
    print(f'{key} = Ключ', end='\n')
    print(f'{value} = Значение', end='\n')
# 2
data['ETH']['total_diff'] = 100
# 3
data['tokens'][0]['fst_token_info']['name'] = 'doge'
# 4
meaning = data['tokens'][0].pop('total_out')
data['tokens'][1].pop('total_out')
data['ETH']['totalOut'] = meaning
# 5
data["tokens"][1]["sec_token_info"]["total_price"] =\
    data["tokens"][1]["sec_token_info"]["price"]
del data["tokens"][1]["sec_token_info"]["price"]
###################################################################################################
# pk 19.4
goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}


store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for key_number, value in goods.items():
    price = 0
    data = {}
    quantity = 0
    for key in store[value]:
        data = key['quantity'] * key['price']
        number = key['quantity']
        quantity += number
        price += data
    print(f'{key_number} - {quantity} штук, стоимость {price} руб.')

##################################################################################
# 19.5
text = input('Введите текст: ').lower()
result = dict()
data = {}

for symbol in text:
    if symbol in result:
        result[symbol] += 1
    else:
        result[symbol] = 1

for i in sorted(result.keys()):
    data[i] = result[i]

for key, value in data.items():
    print(f'{key}:{value}')

one_symbol = [symbol for symbol in data.keys() if data[symbol] == 1]
two_symbol = [symbol for symbol in data.keys() if data[symbol] == 2]
three_symbol = [symbol for symbol in data.keys() if data[symbol] == 3]
print(f'\nИнвертированный словарь частот: \n{one_symbol} \n{two_symbol} \n{three_symbol}')
############################################################################################
#19.6 PK
line_number = {
    1: 'первая',
    2: 'вторая',
    3: 'третья'
}
data_pairs = {}
number_of_pairs = int(input('Введите количество пар слов: '))
for pairs in range(number_of_pairs):
    data = input(f'{line_number[pairs + 1]} пара: ').split()
    data.remove('-')
    data_pairs[data[0]] = data[1]

flag = True
while flag:
    word = input('Введите слово: ').title()
    for key, value in data_pairs.items():
        if key in word:
            print(f'Cиноним: {value}')
            flag = False
            break
        if value in word:
            print(f'Cиноним: {key}')
            flag = False
            break
    else:
        print('Такого слова в словаре нет.')
##########################################################################
#19.7
number_of_orders = int(input('Введите количество заказов: '))
number_text = {
    1: 'Первый',
    2: 'Второй',
    3: 'Третий',
    4: 'Четвертый',
    5: 'Пятый',
    6: 'Шестой'
}
roster = {}
for number_order in range(number_of_orders):
    order = input(f'{number_text[number_order + 1]} заказ: ').split()
    flag = True
    if order[0] in roster:
        for key_surname, value_pizza in roster.items():
            if order[1] in value_pizza and order[0] == key_surname:
                for num in value_pizza.values():
                    summ_pizza = int(num) + int(order[2])
                    roster[order[0]].update({order[1]: summ_pizza})
                    flag = False
                    break
            else:
                if flag:
                    roster[order[0]].update({order[1]: order[2]})
                    break
    else:
        roster[order[0]] = {order[1]: order[2]}

for surname, order_value in sorted(roster.items()):
    print(surname)
    for pizza, number in sorted(order_value.items()):
        print(f'     {pizza}: {number}')

###############################################################################
#19.8
import random
max_number = int(input('Введите максимальное число: '))
intended_number_artem = random.randint(1, max_number)
print(f'--Задуманное число Артема-- {intended_number_artem}')

data_false = set()
data_true = set()
option = {}
while True:
    option = input('Нужное число есть среди вот этих чисел: ').lower().split(' ')
    if option == ['помогите!']:
        data_true.difference_update(data_false)
        print(f'Артём мог загадать следующие числа: {data_true}')
        break
    if str(intended_number_artem) in option:
        data_true = {symbol for symbol in option}
        print('Ответ Артёма: Да', data_true)
    if str(intended_number_artem) not in option:
        data_false = {symbol for symbol in option}
        print('Ответ Артёма: Нет')
#########################################################################
#19.9
couple = {
    1: 'Первая пара',
    2: 'Вторая пара',
    3: 'Третья пара',
    4: 'Четвертая пара',
    5: 'Пятая пара',
    6: 'Шестая пара',
    7: 'Седьмая пара',
    8: 'Восьмая пара',
}
number_people = int(input('Введите количество человек: '))
family_roster = {}
heir_and_parent = {}
roster = dict()
for number in range(1, number_people):
    heir_and_parent = input(f'{couple[number]}: ').split(' ')
    flag = True
    for parent, generation in family_roster.items():
        if parent == heir_and_parent[1] and parent != 'Peter_I':
            roster = {heir_and_parent[0]: generation + 1}
            family_roster.update(roster)
            flag = False
            break
    if flag:
        roster = {heir_and_parent[0]: 1, heir_and_parent[1]: 0}
        family_roster.update(roster)


for parent, generation in sorted(family_roster.items()):
    print(parent, generation)


# Первая пара: Alexei Peter_I
# Вторая пара: Anna Peter_I
# Третья пара: Elizabeth Peter_I
# Четвёртая пара: Peter_II Alexei
# Пятая пара: Peter_III Anna
# Шестая пара: Paul_I Peter_III
# Седьмая пара: Alexander_I Paul_I
# Восьмая пара: Nicholaus_I Paul_I
#########################################################################
#19.10
def get_input_parameters():
    text = input('Введите строку: ')
    return text


def display_result(text_palindrome):
    if text_palindrome:
        print('Можно сделать палиндромом')
    else:
        print('Нельзя сделать палиндромом')


def check_palindrome(old_word):
    temp_old_word = list(old_word)
    for _ in range(len(temp_old_word)):
        letter = temp_old_word.pop()
        temp_old_word.insert(0, letter)
        word_palindrome = temp_old_word[::-1]
        if word_palindrome == temp_old_word:
            word_palindrome = True
            return word_palindrome


if __name__ == '__main__':
    word = get_input_parameters()  # получаем параметры
    is_palindrome = check_palindrome(word)  # является ли слово палиндромом.
    display_result(is_palindrome)  # выводим результат
#########################################################################################
#20.1
import random

numbers_1 = [random.randint(0, 5) for _ in range(10)]
numbers_1 = tuple(numbers_1)

numbers_2 = [random.randint(-5, 0) for _ in range(10)]
numbers_2 = tuple(numbers_2)

answer = numbers_2 + numbers_1
print(f'Кортеж: {answer}')
print(f'Кол-во нулей: {answer.count(0)}')
###########################################################################################
#20.2
import math


def pl_s(r, h):
    side = (2 * math.pi) * r * h
    s_s = math.pi * r ** 2
    full = side + 2 * s_s
    return side, full


radius = int(input('Введите радиус: '))
hight = int(input('Введите высоту: '))
answer_side, answer_full = pl_s(radius, hight)
print(answer_side, answer_full)
#############################################################################
#20.3

import random


def change(nums):
    index = random.randint(0, 4) #или (0, 5) % len(nums)
    value = random.randint(100, 1000)
    nums = list(nums)
    nums[index] = value
    return tuple(nums), value


my_nums = 1, 2, 3, 4, 5

new_nums, rand_val = change(my_nums)
print(new_nums, rand_val)
new_nums_2, rand_val_2 = change(new_nums)
rand_val += rand_val_2
print(new_nums_2, rand_val)
########################################################
#20.2.1
text = input('Строка: ')
text = list(text)
for index, value in enumerate(text):
    if value == '~':
        print('Ответ: ', index, end=' ')
#######################################################
#20.2.2
import random


alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphabet = list(alphabet)
first_roster = [alphabet[random.randint(0, 32)] for _ in range(10)]
second_roster = [alphabet[random.randint(0, 32)] for _ in range(10)]
rosters = {
    0: first_roster,
    1: second_roster
}
new_roster = {}

print('Первый список: ', first_roster)
print('Второй список: ', second_roster)
for num_index, roster in rosters.items():
    for index, value in enumerate(roster):
        new_roster[index] = value
    print(f'{num_index + 1} словарь: {new_roster}')
#############################################################################
#20.2.3
def func(word):
    answer = []
    for i, v in enumerate(word):
        if i % 2 == 0:
            answer.append(v)
    print(answer)

# text_1 = input('Допустим, есть такая строка: ')
# flag = isinstance(text_1, str)
# if flag:
#     func(text_1)
#
# text_2 = input('Допустим, есть такой список: ').split()
# flag = isinstance(text_2, list)
# if flag:
#     func(text_2)

# text_3 = input('Допустим, есть такой кортеж: ')
# text_3 = tuple(text_3)
# flag = isinstance(text_3, tuple)
# if flag:
#     func(text_3)
print(func('О Дивный Новый мир!'))
print(func([100, 200, 300, 'буква', 0, 2, 'а']))
print(func({0: 'е', 1: 'о', 2: 'ч', 3: 'ы', 4: 'в', 5: 'н', 6: 'д', 7: 'а', 8: 'ш', 9: 'ц'}))
###############################################################################################
#20.4.1
incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}

for i_fruit, i_price in incomes.items():
    print(f'{i_fruit} -- {i_price}')
###################################################################
#20.4.2
server_data = {
    "server": {
        "host": "127.0.0.1",
        "port": "10"
    },
    "configuration": {
        "access": "true",
        "login": "Ivan",
        "password": "qwerty"
    }
}

for i_object, value in server_data.items():
    print(f'{i_object}:')
    for i_key, i_value in value.items():
        print(f'     {i_key}: {i_value}')
#############################################################
#20.4.3
print([i_value for i_key, i_value in {0: 0, 1: 100, 2: 144, 3: 20, 4: 19}.items() if i_key % 2 == 0])
##############################################################
#20.5.1
data = {
    (5000, 123456): ('Иванов', 'Василий'),
    (6000, 111111): ('Иванов', 'Петр'),
    (7000, 222222): ('Медведев', 'Алексей'),
    (8000, 333333): ('Алексеев', 'Георгий'),
    (9000, 444444): ('Георгиева', 'Мария')
}
while True:
    series = int(input('Введите серию паспорта: '))
    for i_series, i_name in data.items():
        if series in i_series:
            num = int(input('Введите номер паспорта: '))
            if i_series[1] == num:
                print(f'{i_name[0]} - {i_name[1]}')
#######################################################################
# 20.5.2
roster = {}
while True:
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    phone = int(input('Введите номер телефона: '))
    if (name, surname) in roster:
        print('Этот человек уже есть в базе данных')
        flag = int(input('Нажмите 1 для обновления данных или другую цифру - чтобы не обновлять: '))
        if flag == 1:
            roster[(name, surname)] = phone
        else:
            break
    else:
        roster[(name, surname)] = phone
    print(roster)
#######################################################################################################
# PK 20.1
students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def writes_out_interests(roster_students):
    new_roster_interests = []
    surnames = ''
    for student_id in roster_students:
        surnames += roster_students[student_id]['surname']
        new_roster_interests += (roster_students[student_id]['interests'])
    count_letter = len(surnames)
    new_roster_interests = set(new_roster_interests)
    return count_letter, new_roster_interests


pairs = []
for id_student in students:
    pairs.append((id_student, students[id_student]['age']))

the_number_of_letters_in_the_surname = writes_out_interests(students)[0]
new_roster = writes_out_interests(students)[1]

print(f'Список пар "ID студента — возраст": {pairs}')
print(f'Полный список интересов всех студентов: {new_roster}')
print(f'Общая длина всех фамилий студентов: {the_number_of_letters_in_the_surname}')
########################################################################################
# PK 20.2
def data(entering):
    return [letter for i, letter in enumerate(entering) if i in is_prime(entering)]


def is_prime(enter):
    number_of_characters = len(enter)
    index_letters = []
    for digit_letters in range(2, number_of_characters):
        for number_index in index_letters:
            if digit_letters % number_index == 0:
                break
        else:
            index_letters.append(digit_letters)
    return index_letters


print(data([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # cписок
print(data((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))  # Кортеж
print(data('О Дивный Новый мир!'))  # cтрока
##########################################################################
# PK 20.3
def slicer(number, number_2):
    answer = tuple()
    count = 0
    for num in number:
        if num == number_2:
            count += 1
        if 1 == count:
            answer += (num,)
        if count == 2:
            answer += (num,)
            break
    print(answer)


#print(slicer((1, 9, 3, 4, 5, 6, 7, 8, 2, 2, 10), 9))
###############################################################################
# PK 20.4
players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

roster = [(key + value) for key, value in players.items()] #for k in key for v in value
print(roster)
###############################################################################
# PK 20.5
family = {
    ("Быков", "Павел"): 50,
    ("Быкова", "Ирина"): 38,
    ("Быков", "Игорь"): 71,
    ("Фролова", "Оксана"): 48
}

surname = input('Введите фамилию: ').title()
for sur, year in family.items():
    surname = surname + 'а'
    if surname.startswith(sur):
        print(f'{sur[0]} {sur[1]} {year}')

####################################################
# PK 20.6
import random

roster = [random.randint(0, 10) for num in range(10)]
print(f'Оригинальный список: {roster}')

new_roster = [(roster[index - 1], number) for index, number in enumerate(roster) if index % 2 == 1]
print(f'Новый список (1): {new_roster}')

new_roster_2 = [(roster[number], roster[number + 1]) for number in range(0, len(roster), 2)]
print(f'Новый список (2): {new_roster_2}')
#############################################################
# PK 20.7
def tpl_sort(number):
    answer = tuple()
    flag = True
    for i in number:
        if type(i) == int:
            answer = sorted(number)
        else:
            flag = False
            return number
    if flag:
        answer = tuple(answer)
        return answer


print(tpl_sort((6, 3, -1, 8, 4, 10, -5)))
##############################################################
# PK 20.8
def displays_the_main_menu():
    print(
        'Введите номер действия: \
       \n1. Добавить контакт\
       \n2. Найти человека '
    )
    action_number = int(input())
    if action_number == 1:
        adds_a_contact()
    if action_number == 2:
        finds_a_person()


def adds_a_contact():
    sur_name = input('Введите имя и фамилию нового контакта (через пробел): ').title().split()
    surname, name = sur_name
    if (surname, name) in roster:
        print('Такой человек уже есть в контактах.')
    else:
        number_phone = int(input('Введите номер телефона: '))
        roster[(surname, name)] = number_phone
    print(f'Текущий словарь контактов: {roster}')
    displays_the_main_menu()


def finds_a_person():
    search_surname = input('Введите фамилию для поиска: ').title()
    for surname, number_phone in roster.items():
        if search_surname in surname:
            print(f'{surname[0]} {surname[1]} {number_phone}')
        else:
            print('Такого человека у нас нет')
            displays_the_main_menu()


roster = {}
displays_the_main_menu()
######################################################################
# 20. 9
roster = dict()
count = 0
number_of_protocols = int(input('Сколько записей вносится в протокол? '))
print('Записи (результат и имя):')
for number in range(1, number_of_protocols + 1):
    count += 1
    result_and_name = input(f'{number}-я запись: ').split()
    for name, score in roster.items():
        if result_and_name[1] == name and int(score[0]) >= int(result_and_name[0]):
            break
    else:
        roster[result_and_name[1]] = (int(result_and_name[0]), count)
# roster = {'Jack': (95715, 6), 'qwerty': (197128, 5), 'Alex': (95715, 3), 'M': (95715, 9)}
# Вторая часть задачи решена не в самом лучше свете, это то что пришло в голову...)
if len(roster) > 2:
    count_2 = 1
    print('Итоги соревнований:')
    win = max(roster.items())
    print(f'{count_2}-e место. {win[0]} {win[1][0]}', end='\n')
    roster.pop(win[0])
    winners = sorted(roster.items(), reverse=False)
    for number, key in enumerate(winners):
        count_2 += 1
        if number == 2:
            break
        else:
            print(f'{count_2}-e место. {key[0]} {key[1][0]}', end='\n')

else:
    print('Игроков не может быть меньше 3-ех!')

###################################################################################
# 20. 10
text = 'abcd'
set_number = (10, 20, 30, 40)

answer = ((text[index], set_number[index]) for index in range(min(len(text), len(set_number))))
print(answer)
for pairs in answer:
    print(pairs)

print('Все остальные виды ')
answer = [{text[index], set_number[index]} for index in range(min(len(text), len(set_number)))]
print(answer)

answer = [{text[index]: set_number[index]} for index in range(min(len(text), len(set_number)))]
print(answer)

answer = [(text[index], set_number[index]) for index in range(min(len(text), len(set_number)))]
print(answer)

answer = [[text[index], set_number[index]] for index in range(min(len(text), len(set_number)))]
print(answer)

zipped = dict(zip(text, set_number))
print(zipped)

zipped = set(zip(text, set_number))
print(zipped)

zipped = list(zip(text, set_number))
print(zipped)
########################################################################################################
#21.1
def factorial(number):
    if number == 1:
        return 1
    return number * factorial(number - 1)


answer = factorial(5)
print(answer)
###########################################################################################
#21.2
def power(a, n):
    if n == 1:
        return a
    return a * power(a, n - 1)


float_num = float(input('Введите вещественное число: '))
int_num = int(input('Введите степень числа: '))
print(float_num, '**', int_num, '=', power(float_num, int_num))
###########################################################################################
# 21.3
site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def search_value(website, key):
    if key in website:
        return website[key]
    for branch in website.values():
        if isinstance(branch, dict):
            answer_2 = search_value(branch, key)
            if answer_2:
                break
    else:
        answer_2 = None
    return answer_2


the_desired_value = input('Искомый ключ: ')
answer = search_value(site, the_desired_value)
if answer:
    print(answer)
else:
    print('Такого ключа в структуре сайта нет')
###########################################################################################
# Рекурсия
def foo(x):
    if x == 0:
        print("Вызов foo(0) возвращает 0")
        return 0
    else:
        print(f"Вызов foo({x - 1}) начинается и добавляется в стек")
        new_result = foo(x - 1)
        print(f"Вызов foo({x - 1}) завершился и удаляется из стека")
        result = x + new_result
        print(f'резалт = {result}')
        return result


print(f"Вызов foo(-2) начинается и добавляется в стек")
result = foo(2)
print(f"Вызов foo(2) завершается и удаляется из стека")
print("Итоговый ответ — ", result)
#############################################################################
#21.4
import random


def change_dict(dct):
    num = random.randint(1, 100)
    for i_key, i_value in dct.items():
        if isinstance(i_value, list):
            i_value.append(num)
        if isinstance(i_value, dict):
            i_value[num] = i_key
        if isinstance(i_value, set):
            i_value.add(num)


nums_list = [1, 2, 3]
some_dict = {1: 'text', 2: 'another text'}
uniq_nums = {1, 2, 3}

a = nums_list[:]
b = some_dict.copy()
c = uniq_nums.copy()
common_dict = {1: a, 2: b, 3: c, 4: (10, 20, 30)}
# cделали копию каждому, чтобы в первоначальных значениях - не менялось
change_dict(common_dict)
print(common_dict)

print(nums_list)
print(some_dict)
print(uniq_nums)
#-----------------------------------------------------------------------------------------------
common_dict = {1: nums_list.copy(), 2: some_dict.copy(), 3: uniq_nums.copy(), 4: (10, 20, 30)}
change_dict(common_dict)
print(common_dict)
# Либо мы можем применить вспомогательную функцию, которая сделает это за нас:
import copy

common_dict = {1: nums_list, 2: some_dict, 3: uniq_nums, 4: (10, 20, 30)}
common_dict_2 = copy.deepcopy(common_dict)  # Она будет особенно полезна в структурах, в которых множество вложенных переменных
change_dict(common_dict_2)
print(common_dict_2)

print(nums_list, some_dict, uniq_nums)
##################################################################################
data_names_dict = {
    "<class 'str'>": "строка",
    "<class 'dict'>": "словарь",
    "<class 'list'>": "список",
    "<class 'set'>": "множество"
}

mutable_check_helper = {
    "mutable": ("словарь", "список", "множество")
}


def check_info(data):
    type_of_data = type(data)
    name_of_data = ""
    if str(type_of_data) in data_names_dict:
        name_of_data = data_names_dict[str(type_of_data)]

    if name_of_data in mutable_check_helper["mutable"]:
        property_of_data = "Изменяемый (mutable)"
    else:
        property_of_data = "Неизменяемый (immutable)"

    print(f"Тип данных: {type_of_data} ({name_of_data})")
    print(property_of_data)
    print("Id объекта:", id(data))


data_in = ("g", 'j', "gh")
check_info(data_in)
##############################################################################
#Измерить память
import sys

test = 'привет'
test_tuple = {5: 44, 6: 33, 7: 55}

print(sys.getsizeof((test)))
print(sys.getsizeof((test_tuple)))
#####################################################################################
#Пример Копирования
# >>> import copy
# >>> test_1 = [1, 2, 3, [1, 2, 3]]
# >>> test_copy = copy.copy(test_1)
# >>> print(test_1, test_copy)
# [1, 2, 3, [1, 2, 3]] [1, 2, 3, [1, 2, 3]]
# >>> test_copy[3].append(4)
# >>> print(test_1, test_copy)
# [1, 2, 3, [1, 2, 3, 4]] [1, 2, 3, [1, 2, 3, 4]]
# >>> test_1 = [1, 2, 3, [1, 2, 3]]
# >>> test_deepcopy = copy.deepcopy(test_1)
# >>> test_deepcopy[3].append(4)
# >>> print(test_1, test_deepcopy)
# [1, 2, 3, [1, 2, 3]] [1, 2, 3, [1, 2, 3, 4]]


list_of_lists = [1, 3, 6, 8, 9] # Если объект не сложный и копировать срезом, то в принте - ответы разные
list_of_lists_2 = copy.copy(list_of_lists)#или list_of_lists[:]  # Если обьект сложный- то лучше копировать глубоким(Deepcopy)
list_of_lists[1] = 10
print(list_of_lists)
print(list_of_lists_2)

list_of_lists = [[1, 2, 3], 4, [5, 6, 7]]
list_of_lists_2 = copy.deepcopy(list_of_lists)
list_of_lists[0][0] = 10
print(list_of_lists) #[[10, 2, 3], 4, [5, 6, 7]]
print(list_of_lists_2) #[[1, 2, 3], 4, [5, 6, 7]]

#############################################################################
#21.6
def file_operation(first_argument,
                   two_argument='Неверный ввод. Пожалуйста, введите \'да\' или \'нет\'.',
                   count_attempts=4
                   ):
    while True:
        text = input(first_argument).lower()
        if text == 'да':
            return 1
        if text == 'нет':
            return 0
        else:
            print(two_argument)
        count_attempts -= 1
        if count_attempts == 0:
            print('Попытки иссякли!')
            break
        print(f'Осталось попыток {count_attempts}')


file_operation('Вы действительно хотите выйти? ')
file_operation('Удалить файл? ', 'Так удалить или нет? ')
file_operation('Записать файл? ', count_attempts=2)
##########################################################################
#21.6
def add_num(num, nums=[]):
    nums.append(num)
    print(nums)


add_num(5)
add_num(10)
add_num(15)


def add_num(num, nums=None):
    nums = nums or []
    # хитрая конструкция, которая позволит упростить ввод:
    # if not nums:
    #    nums = []
    # Первый вариант будет выбран, если nums не равен None, иначе будет создан и записан пустой список
    nums.append(num)
    print(nums)


add_num(5)
add_num(10)
add_num(15)
#######################################################################################################
#21.6.3
def create_dict(data, template=None):
    if isinstance(data, dict):
        return data
    if isinstance(data, int) or isinstance(data, float) or isinstance(data, str):
        if not template:
            template = dict()
            template[data] = data
            return template
        else:
            return None


def data_preparation(old_list):
    new_list = []
    for i_element in old_list:
        new_elem = create_dict(i_element)
        if new_elem:
            new_list.append(new_elem)
    return new_list


data_1 = ['sad', {'sds': 23}, {43}, [12, 42, 1], 2323]
data = data_preparation(data_1)

print(data)
##############################################################################################
#pk 21.1
def outputs_the_numbers_in_order(first_number):
    if first_number == 0:
        return first_number
    else:
        outputs_the_numbers_in_order(first_number - 1)
        print(first_number)


number = int(input('Введите число:'))
outputs_the_numbers_in_order(number)
################################################################################
#pk21.2
def do_zip_two(first_data, second_data):
    result = ((first_data[index], second_data[index]) for index in range(min(len(first_data), len(second_data))))
    return result


answer = do_zip_two(first_data=[{'h': 9}, 'b', 'v', 'u'], second_data=(30, {40, }, [90], 'p'))
print(answer) #Если раскрыть генератор то-> [({'h': 9}, 30), ('b', {40}), ('v', [90]), ('u', 'p')]
#####################################################################################
#pk 21.3
def fibonacci(figure):
    if figure < 2:
        return figure
    else:
        return fibonacci(figure - 1) + fibonacci(figure - 2)


number = int(input('Введите позицию числа в ряде Фибоначчи: '))
result = fibonacci(number)
print(f'Число: {result}')
######################################################################################
#pk 21.4

site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def search_value(website, key, count_depth):
    if key in website:
        return website[key]
    for branch in website.values():
        count_depth -= 1
        if isinstance(branch, dict):
            result = search_value(branch, key, count_depth)
            if result and count_depth >= 1:
                break
    else:
        result = None
    return result


def input_data():
    the_desired_value = input('Искомый ключ: ')
    question_max_depth = input('Хотите ввести максимальную глубину? Y/N:').lower()
    if question_max_depth == 'n':
        answer = search_value(site, the_desired_value, 100)
        if answer:
            print(f'Значение ключа: {answer}')
        else:
            print('Такого ключа в структуре сайта нет')

    if question_max_depth == 'y':
        max_depth = int(input('Введите максимальную глубину:'))
        answer = search_value(site, the_desired_value, max_depth)
        if answer:
            print(f'Значение ключа: {answer}')
        else:
            print('Такого ключа в структуре сайта нет')


input_data()
########################################################################
#pk 21.5
def calculating_math_func(data, second_data, base=dict()):
    if second_data not in base:
        if data < second_data:
            for index in range(data, second_data + 1):
                data *= index
                base.update({index: (data / second_data ** 3) ** 10})
            data = second_data
            return base, data
    else:
        return [base[i] for i in range(data, second_data + 1)]


while True:
    first_number = int(input('Введите начальное число: '))
    finish_number = int(input('Введите конечное число: '))
    answer = calculating_math_func(first_number, finish_number)
    print(answer)
########################################################################
#pk 21.6
import copy


def replacing_the_brand_name(copy_struct, brand):
    signboard = f'Сайт для {brand}: '
    copy_struct['html']['head']['title'] = f'Куплю/продам {brand} недорого'
    copy_struct['html']['body']['h2'] = f'У нас самая низкая цена на телефон {brand}'

    return signboard, copy_struct


site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на телефон',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}

number_of_site = int(input('Сколько сайтов: '))
result = []
for _ in range(number_of_site):
    name_brand = input('\nВведите название продукта для нового сайта: ')
    copy_site = copy.deepcopy(site)
    answer = replacing_the_brand_name(copy_site, name_brand)
    result.append(answer)
    for index_result in result:
        print(f'\n{index_result}')
########################################################################
#pk 21.7
def advanced_sum_function(numbers_list, answer):
    if isinstance(numbers_list, tuple):
        answer = [number for number in numbers_list]
        return sum(answer)
    if isinstance(numbers_list, list):
        for number in numbers_list:
            if not isinstance(number, list):
                answer.append(number)
            advanced_sum_function(number, answer)
    return sum(answer)


tuple_numbers = advanced_sum_function((1, 2, 3, 4, 5), answer=[])
list_numbers = advanced_sum_function(([[1, 2, [3]], [1], 3]), answer=[])
print(tuple_numbers)
print(list_numbers)
########################################################################
#pk 21.8

def advanced_sum_function_2(numbers_list, answer):
    if isinstance(numbers_list, list):
        for number in numbers_list:
            if not isinstance(number, list):
                answer.append(number)
            advanced_sum_function_2(number, answer)
    return answer


list_numbers = advanced_sum_function_2(
    ([1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]),
    answer=[]
    )
print(list_numbers)
########################################################################
#pk 21.9
def the_hanoi_towers_algorithm(disks, start, finish):
    if disks <= 0:
        return
    temp = 6 - start - finish
    the_hanoi_towers_algorithm(disks - 1, start, temp)
    print(f'Переложить диск {disks} со стержня номер {start} на стержень номер {finish}')
    the_hanoi_towers_algorithm(disks - 1, temp, finish)


number_of_disks = int(input('Введите количество дисков: '))
the_hanoi_towers_algorithm(number_of_disks, 1, 3)

########################################################################
import os
# 22.3
# Корень диска: G:\
# c разными вариациями...

print("Корень диска:", os.path.abspath('.').split("\\")[0])
print('Корень диска:', os.path.abspath(os.path.join('\\')))
print('Корень диска:', os.path.abspath(os.path.join('.', '\\')))
print('Корень диска:', os.path.abspath(os.path.join('.', '\\')[0]))
print('Корень диска:', os.path.abspath(os.path.join('..', '\\')[0]))
print("Корень диска:", os.path.abspath('.').split("\\")[0])
print(os.getcwd())
print(os.path.abspath('..'))
print(os.path)

# 22.2
import os

def print_dirs(project):
    print('\nСодержимое папки:', project)
    for i_elem in os.listdir(project):
        new_path = os.path.join(project, i_elem)
        print('    ', new_path)


name_folder = ['Temp_work', 'Skillbox']
for i_folder in name_folder:
    path_project = os.path.abspath(os.path.join('..', i_folder))
    print_dirs(path_project)

# 22.1
import os

#Примечание: при работе с путями не прописывайте слеши вручную, генерация должна быть программной.
rel_path = os.path.join('Skillbox', 'access', 'admin.bat')
print(rel_path) #Относительный путь до файла
abs_path = os.path.abspath(os.path.join('..', rel_path))
print(abs_path) #Абсолютный путь до файла

#CMD
# os.path.abspath('new_folder')
#
# 'C:\\Users\\bykovap\\PycharmProjects\\Temp_work\\new_folder'
# os.path.abspath('../new_folder')
# 'C:\\Users\\bykovap\\PycharmProjects\\new_folder'
# os.path.abspath(os.path.join('../new_folder'))
# 'C:\\Users\\bykovap\\PycharmProjects\\new_folder'
# os.path.abspath(os.path.join('..', 'new_folder'))
# 'C:\\Users\\bykovap\\PycharmProjects\\new_folder'
# os.path.abspath('/new_folder')
# 'C:\\new_folder'
# os.path.abspath(os.path.join(os.path.sep,'new_folder'))
# 'C:\\new_folder'
# os.path.abspath(os.path.join(os.path.sep,'new_folder'))
# 'C:\\new_folder'
######################################################################################################
import os


def project_dir(path_project):
    print(f'Cодержимое папки: {path_project}')
    if os.path.exists(path_project):
        for elem in os.listdir(path_project):
            print('    ', os.path.join(path_project, elem))
    else:
        print('Такой папки не существует')


projects = ['Temp_work', 'PycharmProjects', 'Skill']
for project in projects:
    path = os.path.abspath(os.path.join('..', project))
    project_dir(path)
#################################################################################################
import os


def project_dir(path_project):
    print(f'Cодержимое папки: {path_project}')
    if os.path.exists(path_project):
        for elem in os.listdir(path_project):
            print('    ', os.path.join(path_project, elem))
    else:
        print('Такой папки не существует')


projects = ['Temp_work', 'PycharmProjects', 'Skill']
for project in projects:
    path = os.path.abspath(os.path.join('..', project))
    project_dir(path)

#########################################################################################
import os


def find_file(cur_path, file_name):
    print('переходим', cur_path)

    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        print('     cмотрим', path)
        if file_name == i_elem:
            return path
        if os.path.isdir(path):
            print('Это директория', )
            result = find_file(path, file_name)
            if result:
                break
    else:
        result = None

    return result


find_path = find_file(os.path.abspath(os.path.join('..', '..', 'PycharmProjects')), 'main.py')
if find_path:
    print(f'Абсолютный путь к файлу: {find_path}')
else:
    print('Файл не найден.')

########################################################################################3
import os


def find_file(cur_path, file_name):
    print('переходим', cur_path)

    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        print('     cмотрим', path)
        if file_name == i_elem:
            return path
        if os.path.isdir(path):
            print('Это директория', )
            result = find_file(path, file_name)
            if result:
                break
    else:
        result = None

    return result


find_path = find_file(os.path.abspath(os.path.join('..', '..', 'PycharmProjects')), 'main.py')
if find_path:
    print(f'Абсолютный путь к файлу: {find_path}')
else:
    print('Файл не найден.')

#############################################################################################
#22.2.2
import os


def find_file(cur_path, file_name):
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        if file_name == i_elem:
            print(f'     {path}')
        if os.path.isdir(path):
            result = find_file(path, file_name)
            if result:
                break
        # else:     ПОИДЕИ работает и без этого, но наверно надо оставить
        #     result = None
        #
        # return result


search_address = input('Ищем в: ')
name_file = input('Имя файла: ')
print('Найдены следующие пути:')
find_file(search_address, name_file)
##############################################################################################
#ОТКРЫТЬ
file = open('speakers.txt')
data = file.read()

for i in data:
    print(i, end='')
###################################################################
#22.3.1 #DВторой варианть
import os

address_file_1 = os.path.join('task', 'group_1.txt')
address_file_2 = os.path.join('task', 'Additional_info', 'group_2.txt.txt')

first_file = open(address_file_1, 'r')
second_file = open(address_file_2, 'r')
summa = 0
diff = 0
compose = 1

for i_line in first_file:
    info = i_line.split()
    if info:
        summa += int(info[2])
        diff -= int(info[2])
first_file.close()


for i_line in second_file:
    info = i_line.split()
    if info:
        compose *= int(info[2])
second_file.close()

print(f'Cумма первой группы: {summa}')
print(f'Разность первой группы: {diff}')
print(f'Произведение второй группы: {compose}')
################################################################################
#22.3.2
import random
import os


def find_file(cur_path, file_name, roster_path):
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        if file_name == i_elem:
            roster_path.append(path)
        if os.path.isdir(path):
            result = find_file(path, file_name, roster_path)
            if result:
                break


roster = []
search_address = os.path.abspath(os.path.join(''))
name_file = input('Имя файла: ')
print('Найдены следующие пути:')
find_file(search_address, name_file, roster)
random_numbers = random.randint(0, len(roster)-1)
data_file = open(roster[random_numbers], 'r')
for elem in data_file:
    print(elem, end='')
######################################################################################
#Показывает содердимое файлов
# def print_dirs(project):
#     print('\nСодержимое папки:', project)
#     for i_elem in os.listdir(project):
#         new_path = os.path.join(project, i_elem)
#         print('    ', new_path)
#
#
# name_folder = ['Temp_work', 'Skillbox']
# for i_folder in name_folder:
#     path_project = os.path.abspath(os.path.join('..', i_folder))
#     print_dirs(path_project)

for path in os.listdir('..'):
    print(os.path.join(os.path.abspath('..'), path))

#######################################################################
#9.4.1 Метод write. Режимы записи
numbers_file = open('numbers.txt', 'r')
summ_numbers = 0
for symbol in numbers_file:
    number = symbol.split('\n')
    clear_number = ''.join(number)
    if clear_number.isdigit():
        summ_numbers += int(clear_number)

numbers_file.close()
answer = open('answer.txt', 'w')
answer.write(str(summ_numbers))
answer.close()

########################################################################
#ШЕДЕВР ЗАПИСЫВАЕТ ВСЕ ПАПКИ  ПРАКТИЧЕСКИХ в текстовый документ
#ШЕДЕВР ЗАПИСЫВАЕТ ВСЕ ПАПКИ  ПРАКТИЧЕСКИХ в текстовый документ
#ШЕДЕВР ЗАПИСЫВАЕТ ВСЕ ПАПКИ  ПРАКТИЧЕСКИХ в текстовый документ

import os


def write_homework(address_path, homework_file, new_file):
    for elem in os.listdir(address_path):
        path = os.path.join(address_path, elem)
        if elem == homework_file:
            address_true = open(path, 'r', encoding='utf8')
            new_file.write(f'\n{path}')
            new_file.write('\n')
            for sym in address_true:
                new_file.write(f'{str(sym)}')
            new_file.write('\n')
            new_file.write('#' * 40)
        if os.path.isdir(path):
            result = write_homework(path, homework_file, new_file)
            if result:
                 break


open_new_file = os.path.abspath(os.path.join('homework_SCRIPT.txt'))
file = open(open_new_file, 'w', encoding='utf8')
search_path = os.path.abspath(os.path.join(''))
homework_name_file = ('main.py')
write_homework(search_path, homework_name_file, file)
file.close()
########################################################################
#ШИФР для себя
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
###################################################################
#22.4pk
import os


def print_dirs(project, size_file, subdir):
    for i_elem in os.listdir(project):
        new_path = os.path.join(project, i_elem)
        if os.path.isdir(new_path):
            subdir.append(new_path)
            print_dirs(new_path, size_file, subdir)
        elif os.path.isfile(new_path):
            size = os.path.getsize(new_path)
            size_file.append(size)
    return size_file, subdir


sum_size_file = []
subdirectories = []
address = os.path.abspath(os.path.join('..', '..', 'Module14'))
print(address)
sum_size, subdir = print_dirs(address, sum_size_file, subdirectories)
print(f'Размер каталога (в Кб): {sum(sum_size) / 1024}')
# subdirectories = [directories for directories in os.listdir(address) if os.path.isdir(os.path.join('..', directories))]
# print(f'Количество подкаталогов: {len(subdirectories)}')
print(f'Количество подкаталогов: {len(subdirectories)}')
################################################################################
#22.5pk
import os


def saving_in_a_text_document():
    text = input('Введите строку: ')
    new_path = input('\nКуда хотите сохранить документ?'
                     ' Введите последовательность папок (через пробел): ').split(' ')
    # Users bykovap Skillbox Module22 06_paranoia
    disk_root = os.path.abspath('.').split("\\")[0]
    new_path.insert(0, disk_root)

    new_file = input('\nВведите имя файла: ')
    new_path = '\\'.join(new_path)
    new_address = os.path.join(new_path, new_file)

    if not os.path.exists(new_address):
        open_file = open(new_address, 'w', encoding='utf8')
        open_file.write(text)
        open_file.close()
        print('Файл успешно сохранён!')
    else:
        overwrite = input('Вы действительно хотите перезаписать файл? ').lower()
        if overwrite == 'да':
            open_file = open(new_address, 'w', encoding='utf8')
            open_file.write(text)
            open_file.close()
            print('Файл успешно перезаписан!')
        else:
            pass
    return new_address


result = saving_in_a_text_document()
result = open(result, 'r', encoding='utf8')
print(f'\nСодержимое файла: ')
for text in result:
    print(text)
result.close()
################################################################################
#22.6pk
import os


def start():
    current_folder = os.path.abspath(os.path.join('cipher_text.txt.'))
    new_entry = open(current_folder, 'w', encoding='utf8')
    alphabet_england = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_england = list(alphabet_england)
    file = open('text.txt', 'r', encoding='utf8')
    print('Содержимое файла text.txt: ')
    for number_word, word in enumerate(file):
        new_text = []
        print(word, end='')
        for letter in word:
            if letter.lower() in alphabet_england:
                number_index_letter = alphabet_england.index(letter.lower())
                number_index_letter += number_word + 1  #А если это 30 буква?расписать
                new_text.append(alphabet_england[number_index_letter])
        new_text_str = ''.join(new_text)
        new_entry.write(str(new_text_str) + '\n')
    new_entry.close()
    print('\n')
    print('\nСодержимое файла cipher_text.txt.: ')
    read_file = open('cipher_text.txt.', 'r', encoding='utf8')
    for word in read_file:
        print(word.title(), end='')


start()
################################################################################
#22.7pk
file = open('first_tour.txt').read().split('\n')
temp_scores = 0
data = []

print('Содержимое файла first_tour.txt: ')
for index, elem in enumerate(file):
    roster_str = elem.split(' ')
    print(elem, end='\n')
    if index == 0:
        temp_scores = roster_str
    else:
        if int(roster_str[2]) > int(temp_scores[0]):
            abbreviated_name = ''.join(list(roster_str[1][0] + '.'))
            word = abbreviated_name, roster_str[0], roster_str[2]
            data.append(word)


new_file = open('second_tour.txt', 'w', encoding='utf8')
data = sorted(data, reverse=True)
new_file.write(str(len(data)))
new_file.write('\n')
for index, card_person in enumerate(data):
    new_file.write(str(f'{index + 1}) '))
    new_file.write(str(' '.join(card_person)))
    new_file.write('\n')
new_file.close()
############################################################################################
#22.8pk
file = open('text.txt', 'r', encoding='utf-8')
all_letters = [letter.lower() for word in file for letter in word if letter.isalpha()]


file = open('text.txt', 'r', encoding='utf-8')
sort_letters = {letter.lower() for word in file for letter in word if letter.isalpha()}


file = open('text.txt', 'r', encoding='utf-8')
result = {}
for letter in sort_letters:
    fraction = all_letters.count(letter) / len(all_letters)
    result[letter] = round(fraction, 3)


new_file = open('analysis.txt', 'w', encoding='utf-8')
sorted_rooms = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
for key_letter, value_fraction in sorted_rooms.items():
    new_file.write(key_letter + ' ' + str(value_fraction) + '\n')

new_file.close()
############################################################################################
#23.2.1 hm
BRUCE_WILLIS = 42
input_data = input('Введите строку: ')
try:
    leeloo = int(input_data[4])
    result = BRUCE_WILLIS * leeloo
    print(f'- Leeloo Dallas! Multi-pass № {result}!')

except ValueError as exc:  # as - этот оператор запишет пойманное исключение в переменную exc (название может быть любым)
    print(type(exc), "— невозможно преобразовать к числу")
except IndexError as exc:
    print(type(exc), "— выход за границы списка")
except Exception as exc:
    print(type(exc), "поймано исключение")
############################################################################################
#23.2.2 hm
file = open('age.txt', 'r', encoding='utf-8')
new_file = open('result.txt', 'w', encoding='utf-8')
try:
    for age in file:
        name = input('Введите имя: ')
        name_and_age = (name + '-' + age)
        new_file.write(name_and_age)

    new_file.close()
except FileExistsError as exs:
    print(type(exs), 'Попытка создания файла, который уже существует.')
except IsADirectoryError as exs:
    print(type(exs), 'На чтение ожидался файл, но это оказалась директория.')
except (TypeError, ValueError) as exs:
    print(type(exs), 'Неверный тип данных и некорректное значение (две ошибки обрабатываются одинаково).')
############################################################################################
#23.2.2(1) hm
file_ages = None
file_result = None

try:
    file_ages = open("age.txt", "r", encoding="utf8")
    file_result = open("result.txt", "x", encoding="utf8")
    # режим 'x' - это эксклюзивное создание, бросается исключение FileExistsError, если файл уже существует.
except (FileExistsError, PermissionError) as exc:  # названия исключений можно группировать в кортежи
    print("Поймано исключение: ", exc, type(exc))

if file_result and file_ages:
    names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    count = 0
    for line in file_ages:
        try:
            clear_line = line.rstrip()
            int(clear_line)  # на всякий случай пытаемся преобразить данные в int, но не сохраняем это в переменную,
            # т.к. записывать нам в файл придётся именно строку
            file_result.write(names[count] + " - " + clear_line)
            count += 1
        except (ValueError, TypeError) as exc:
            print("Поймано исключение: ", exc, type(exc))
############################################################################################
#23.3.1
file = None
try:
    file = open("23.3.txt", "w", encoding="utf8")
    number = int(input("Введите текст: "))
    file.write(str(number))
except (FileNotFoundError, PermissionError) as exc:
    print(type(exc), exc)
except ValueError as exc:
    print(type(exc), exc)
except Exception as exc:
    print(type(exc), exc)
else:
    print("Запись прошла без ошибок")
finally:
    if file and not file.closed:
        file.close()
############################################################################################
file = open('people.txt', encoding='utf-8').read().split('\n')
name_roster = []

try:
    for line, name in enumerate(file):
        if name.isalpha():
            if len(name) < 3:
                raise BaseException(f'В строке {line} меньше 3 букв')
            name_roster.append(len(name))


except FileExistsError:
    print('Файл не найден')
finally:
    print('Столько символов: ', sum(name_roster))
############################################################################################
#23.4.2
file = open('words.txt', encoding='utf-8').read().split('\n')
count = 0
try:
    for index, line in enumerate(file):
        temp_old_word = list(line)
        if not line.isalpha():
            raise ValueError(f'строка не полностью состоит из букв! cлово {line} в строке {index + 1}')
        for _ in range(len(temp_old_word)):
            letter = temp_old_word.pop()
            temp_old_word.insert(0, letter)
            word_palindrome = temp_old_word[::-1]
            if word_palindrome == temp_old_word:
                count += 1
except ValueError as exs:
    error_file = open('errors.log', 'w', encoding='utf-8')
    error_file.write(str(exs))
    error_file.close()
finally:
    print(f'Слов палиндромов {count}')

############################################################################################
# Здесь палиндромм получше будет!
def check_palindrome(word):
    return word == word[::-1]


# оператор with из 23.5
with open('words.txt', 'r', encoding='utf8') as file, open('errors.log', 'w', encoding='utf8') as log_file:
    count = 0

    for line in file:
        try:
            clear_line = line.rstrip()
            if clear_line.isalpha():
                count += check_palindrome(clear_line)
            else:
                raise ValueError("строка не полностью состоит из букв!")
        except ValueError as exc:
            log_file.write(str(exc))

    print(count)
##############################################################################
#23.1 PK
with open('people.txt', 'r', encoding='utf8') as file, open('errors.log', 'w', encoding='utf8') as log_file:
    count = 0

    for line, name in enumerate(file):
        try:
            name = name.rstrip()
            count += len(name)
            if len(name) < 3:
                raise BaseException(f'Ошибка: менее трёх символов в строке {line + 1}.')
        except BaseException as exc:
            print(exc)
            log_file.write(str(exc))

    print(f'Общее количество символов: {count}')
##############################################################################
#23.2 PK
import random


def adding_numbers_to_coordinates(x, y):
    x += random.randint(0, 5)
    y += random.randint(0, 10)
    return x / y


def subtract_the_numbers(x, y):
    x -= random.randint(0, 5)
    y -= random.randint(0, 10)
    return y / x


try:
    with open('coordinates.txt', 'r') as file_coordinates, open('result.txt', 'w') as file_answer:
        for line in file_coordinates:
            nums_list = line.split()
            result_adding = adding_numbers_to_coordinates(int(nums_list[0]), int(nums_list[1]))
            result_subtract = subtract_the_numbers(int(nums_list[0]), int(nums_list[1]))
            number = random.randint(0, 100)
            my_list = sorted([result_adding, result_subtract, number])
            file_answer.write(''.join(str(my_list)))
            file_answer.write('\n')
except ZeroDivisionError as exs:
    print(exs, type(exs))
##############################################################################
#23.3 PK
import random

result = 0
try:
    with open('out_file.txt', 'w', encoding='utf-8') as out_file:
        while True:
            number = input('Введите число: ')
            if number.isdigit():
                fortuna = random.randint(1, 13)
                if fortuna == 1:
                    raise BaseException('Вас постигла неудача!')
                out_file.write(number)
                out_file.write('\n')
                result += int(number)
                if result >= 777:
                    raise BaseException('Вы успешно выполнили условие для выхода из порочного цикла!')
            raise TypeError('Вводите цифры!')
except TypeError as exc:
    print(exc)
except BaseException as exc:
    print(exc)
finally:
    print('Содержимое файла out_file.txt:')
    file = open('out_file.txt').read().split('\n')
    for number in file:
        print(number)
##############################################################################
#23.4 PK
data_file = open('registrations.txt', encoding='utf-8').read().split('\n')
with open('registrations_good.log', 'w', encoding='utf-8') as registrations_good_file,\
        open('registrations_bad.log', 'w', encoding='utf-8') as registrations_bad_file:
    for line in data_file:
        split_line = line.split(' ')
        try:
            if len(split_line) == 3:
                if split_line[0].isalpha():
                    if '.' and '@' in split_line[1]:
                        if 99 > int(split_line[2]) > 10:
                            registrations_good_file.write(' '.join(split_line))
                            registrations_good_file.write('\n')
                        else:
                            raise ValueError('Поле «Возраст» НЕ является числом от 10 до 99')
                    else:
                        raise SyntaxError('Поле «Имейл» НЕ содержит @ и .(точку)')
                else:
                    raise NameError('Поле имени содержит НЕ только буквы')
            else:
                raise IndexError('НЕ присутствуют все три поля')
        except Exception as exc:
            registrations_bad_file.write(str(' '.join(split_line)) + ' -- ' + str(exc))
            registrations_bad_file.write('\n')
        else:
            pass
##############################################################################
#23.5 PK
calculate_file = open('calc.txt', encoding='utf-8').read().split('\n')
arithmetic_symbols = ['+', '-', '/', '//', '*', '%']
result = 0
for operation in calculate_file:
    try:
        split_operation = operation.split(' ')
        if split_operation[1] in arithmetic_symbols:
            number = ''.join(split_operation)
            answer = eval(number)
            result += answer
        else:
            mathematical_example = ''.join(split_operation)
            raise BaseException(f'Обнаружена ошибка в строке: {mathematical_example}')
    except BaseException as exc:
        print(exc)
        correction = input('Хотите исправить?').lower()
        if correction == 'да':
            corrected_version = input('Введите исправленную строку: ')
            answer = eval(corrected_version)
            result += answer
        else:
            continue

print(f'Сумма результатов: {result}')
##############################################################################
#23.6 PK
def records_and_displays_the_message():
    print('╔=================================================================╗')
    print('║                          CryptoChat                             ║')
    print('║                                                                 ║')
    print('║                         ГЛАВНОЕ МЕНЮ.                           ║')
    print('║                                                                 ║')
    print('╚=================================================================╝')

    while True:
        try:
            username = input('Введите имя пользователя: ')
            file_username = username + '.txt'
            print('Выберите одно из действии: \n   1.Посмотреть текущий текст чата. \n   2.Отправить сообщение.')
            action = int(input())
            if action == 1:
                file_message = open(file_username, encoding='utf-8').read().split('\n')
                print('Ваш чат')
                for message in file_message:
                    print('-', message)
            if action == 2:
                with open(file_username, 'a', encoding='utf-8') as username_file:
                    message = input('Пиши: ')
                    username_file.write(message)
                    username_file.write('\n')
        except Exception as exc:
            print('Ваш Чат пустой, напиши сначала ему')
            with open('Error.txt', 'w', encoding='utf-8') as log_file:
                log_file.write(str(exc))


records_and_displays_the_message()
##############################################################################
#24.2.1
import random


class Toyota:
    color = 'красный'
    price = 1000000
    max_speed = 200
    current_speed = 0


data_1 = Toyota()
data_1.max_speed = random.randint(0, 200)

data_2 = Toyota()
data_2.max_speed = random.randint(0, 200)

data_3 = Toyota()
data_3.max_speed = random.randint(0, 200)

print(data_1.max_speed, data_2.max_speed, data_3.max_speed)
##############################################################################
#24.2.2
class Monitor:
    name = 'Samsung'
    matrix = 'VA'
    resolution = 'WQHD'
    frequency = 0


class Headphones:
    name = 'Sony'
    sensitivity = 108
    micro = True


monitors = [Monitor() for _ in range(4)]
headphones = [Headphones() for _ in range(3)]


for index, number in enumerate([60, 144, 70, 60]):
    monitors[index].frequency = number

headphones[0].micro = False
##############################################################################
#24.3.1
class Toyota:
    color = 'красный'
    price = 1000000
    max_speed = 200
    current_speed = 0

    def info(self):
        print(f'Color - {self.color}\n'
              f'price - {self.price}\n'
              f'max speed - {self.max_speed}\n'
              f'current speed - {self.current_speed}')

    def set_the_speed(self):
        self.current_speed = int(input('Введите текущую скорость машины: '))

    def speed(self, new_speed):
        self.current_speed = new_speed


data = Toyota()
data.info()
data.set_the_speed()
data.info()
data.speed(200)
data.info()
print(Toyota.current_speed) #обратите внимание, что скорость внутри Класса осталась той же, её изменения не коснулись
##############################################################################
#24.3.2
class Family:
    family_name = 'Common family'
    money = 100000
    have_a_house = False

    def info(self):
        print(
              'Family name: {}\nFamily funds: {}\nFamily funds: {}'.format(
                  self.family_name, self.money, self.have_a_house
              )
        )

    def earn_money(self, add_money):
        self.money += add_money
        print(f'Earned {add_money} money! Current value :{self.money}')

    def buy_a_house(self, house_price, discount=0):
        house_price -= house_price * discount / 100
        if self.money >= house_price:
            self.money -= house_price
            self.have_a_house = True
            print(f'House purchased! Current money: {self.money}\n')
        else:
            print('Not enough money!\n')


family_data = Family()
family_data.info()

print('Try to buy a house')
family_data.buy_a_house(10 ** 6)

if not family_data.have_a_house:
    family_data.earn_money(800000)
    print('Try to buy a house again')
    family_data.buy_a_house(10 ** 6, 10)


family_data.info()
#########################################################################
#24.4.1
class Toyota:

    def __init__(self):
        self.color = 'Красная'
        self.price = '1000000'
        self.max_speed = '200'
        self.current_speed = '0'

    def info(self):
        print(
            f'Цвет: {self.color},'
            f'\nЦена: {self.price},'
            f'\nМаксимальная скорость: {self.max_speed},'
            f'\nТекущая скорость: {self.current_speed} '
        )

    def data_replacement(self, speed):
        self.current_speed = speed


car_toyota = Toyota()
car_toyota.info()
car_toyota.data_replacement(100)
car_toyota.info()
#########################################################################
#24.4.2
class Point:
    count = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        Point.count += 1

    def info(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        print(f'x = {self.x}, y = {self.y}')
        print(f'По счёту это {self.count} точка')


data = Point()
data.info(5, 4)
data_2 = Point()
data_2.info(0, 4)
#########################################################################
#24.4.3
class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зелёная', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print(f'Картошка {self.index} сейчас {Potato.states[self.state]} ')


class Garden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка прорастает')
        for i_potato in self.potatoes:
            i_potato.grow()

    def are_all_ripe(self):
        if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
            print('Картошка еще не созрела!\n')

        else:
            print('Вся картошка созрела. Можно собирать\n')
            return True


my_garden = Garden(5)
for _ in range(3):
    my_garden.grow_all()
    my_garden.are_all_ripe()

#########################################################################
#24.1.PK
import random


class Warrior:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.damage = 20

    def fight(self, person):
        if person.hp > 0:
            person.hp -= self.damage
            person.print_info()

    def print_info(self):
        if self.hp != 0:
            print(f'У Персонажа {self.name} осталось {self.hp}хп')
        else:
            print(f'КОНЕЦ {self.name}')


class Battle:
    def __init__(self):
        self.war_1 = Warrior(warriors[0])
        self.war_2 = Warrior(warriors[1])

    def fight_final(self):
        for _ in range(20):
            if self.war_1.hp == 0 or self.war_2.hp == 0:
                break
            else:
                index_random = random.randint(0, 1)
                if index_random == 0:
                    print(f'\n{warriors[index_random]} наносит удар')
                    self.war_1.fight(self.war_2)
                else:
                    print(f'\n{warriors[index_random]} наносит удар')
                    self.war_2.fight(self.war_1)


warriors = ['Чебурашка', 'Шапокляк']
war_fight = Battle()
war_fight.fight_final()
#########################################################################
#24.2.PK
import random
from operator import itemgetter


class Student:
    all_students = []

    def __init__(self, data_name='Долматов Иван', number_of_group=3, grade=None):
        self.data_name = data_name
        self.number_of_group = number_of_group
        self.grade = grade
        self.all_students = list()

    def adds_students(self):
        Student.all_students.append([self.data_name, self.number_of_group, sorted(self.grade)])

    def print_info(self):
        roster = sorted(Student.all_students, key=itemgetter(2), reverse=True)
        for i_elem in roster:
            self.data_name = i_elem[0]
            self.number_of_group = i_elem[1]
            self.grade = i_elem[2]
            print(f'Ученик {self.data_name} учится в группе {self.number_of_group} c оценками {self.grade}')


for _ in range(10):
    names = ['-', 'Коля', 'Александр', 'Дима', 'Николай', 'Иван']
    surname = ['Брин', 'Долматов', 'Дондуков', 'Быков', 'Иванов', 'Петров', 'Печкин']
    grade_student = [random.randint(2, 5) for _ in range(5)]
    number_random = random.randint(1, 5)
    number_surname = random.randint(0, 6)
    the_name = ''.join(surname[number_surname] + ' ' + names[number_random])
    new_student = Student(the_name, number_random, grade_student)
    new_student.adds_students()


result = Student()
result.print_info()
#########################################################################
#24.3.PK
import math


class Circle:
    def __init__(self, x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.r = r

    def get_perimeter(self):
        answer_perimeter = 2 * math.pi * self.r
        print(answer_perimeter)

    def get_square(self):
        answer_square = math.pi * self.r ** 2
        print(answer_square)

    def increase_scale(self, k):
        self.r *= k
        print(self.r)

    def is_intersect(self, other):
        print((self.x - other.x) ** 2 + (self.y - other.y) ** 2 <= (self.r + other.r) ** 2)


first_data = Circle()
first_data.get_perimeter()
first_data.get_square()
first_data.increase_scale(2)
second_data = Circle(1, 3, 2)
first_data.is_intersect(second_data)
#########################################################################
#24.4.PK (Помогли www) сначала писал более умудренный сложный вариант
import random


def check_age(parent_age, age_kid):
    if age_kid > parent_age - 16:
        print('Возраст не похож на действительный')
        return False
    else:
        return True


class Parent:

    def __init__(self, name_parent, age_parent, roster_of_kids):
        self.name_parent = name_parent
        self.age_parent = age_parent
        self.roster_of_kids = []

    def info_about_parent(self):
        print(f'Меня зовут {self.name_parent}!, возраст мой - {self.age_parent}'
              f' и у меня {len(self.roster_of_kids)} детей')

    def soothe_the_child(self, children):
        if child.state_calm == 1:
            print(f'{self.name_parent}!  {children.name_child} кричит! ')
            child.state_calm = 0
        else:
            print(f'{self.name_parent}! Твоё милое дитя, {children.name_child} в состоянии спокойствия! ')

    def feed_the_child(self, children):
        if child.state_feed == 1:
            print(f'{self.name_parent}!  Твоё милое дитя, {children.name_child} хочет кушать! ')
            child.state_feed = 0
        else:
            print(f'Чудесно, {self.name_parent}! Крошка {children.name_child} кушать не хочет! ')


class Children:
    calmness = {0: 'Спокоен', 1: 'Кричит'}
    hunger = {0: 'Сыт', 1: 'Голоден'}

    def __init__(self, name_child, age_child):
        self.name_child = name_child
        self.age_child = age_child
        self.calmness = 0
        self.hunger = 0

    def info_about_child(self, calm, feed):
        print(f'Дитя {self.name_child} сейчас {Children.calmness[calm]}')
        print(f'Дитя {self.name_child} сейчас {Children.hunger[feed]}')


name_parent = input('Как зовут Вас? ').title()
age_parent = int(input(f'{name_parent} сколько лет? '))
family = Parent(name_parent, age_parent, roster_of_kids=[])

child_name_1 = input('\nКак зовут ребёнка? ').title()
child_age_1 = int(input('Сколько лет ребёнку? '))
if check_age(age_parent, child_age_1):
    data_child = Children(child_name_1, child_age_1)
    family.roster_of_kids.append(data_child)

child_name_2 = input('\nКак зовут ребёнка? ')
child_age_2 = int(input('Сколько лет ребёнку? '))
if check_age(age_parent, child_age_2):
    data_child = Children(child_name_2, child_age_2)
    family.roster_of_kids.append(data_child)

for child in family.roster_of_kids:
    child.state_calm = random.randint(0, 1)
    child.state_feed = random.randint(0, 1)
    child.info_about_child(child.state_calm, child.state_feed)
    family.soothe_the_child(child)
    family.feed_the_child(child)

#########################################################################
#24.5.PK
class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зелёная', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print(f'Картошка {self.index} сейчас {Potato.states[self.state]} ')


class Garden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка прорастает')
        for i_potato in self.potatoes:
            i_potato.grow()

    def are_all_ripe(self):
        if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
            print('Картошка еще не созрела!\n')

        else:
            print('Вся картошка созрела. Можно собирать\n')
            return True


class Gardener:

    def __init__(self, name_gardener, count):
        self.name_gardener = name_gardener
        self.count_potato = count
        self.bed_potatoes = Garden(count)
        self.harvested_potatoes = []

    def care_of_the_garden(self):
        print('Садовник начинает ухаживать за картошкой')
        self.bed_potatoes.grow_all()

    def harvest(self):
        if self.bed_potatoes.are_all_ripe():
            self.harvested_potatoes.append(self.count_potato)
            print(f'Садовник {self.name_gardener} сегодня собрал урожай Картошки! Целых {self.count_potato} шт.')
        else:
            print(f'Еще рано Садовнику {self.name_gardener} собирать урожай! Расти Картошку')


gardener_1 = Gardener('Коля', 5)
for _ in range(3):
    gardener_1.care_of_the_garden()

gardener_1.harvest()
#########################################################################
#24.6.PK
class ElementEarn:
    def __init__(self):
        self.element = 'Земля'

    def __add__(self, other):
        if other == 'Вода':
            return 'Грязь'
        if other == 'Воздух':
            return 'Пыль'
        if other == 'Огонь':
            return 'Лава'
        if other == 'Земля':
            return 'Давление'
        return other + self.element


class ElementWater:
    def __init__(self):
        self.element = 'Вода'

    def __add__(self, other):
        if other == 'Земля':
            return 'Грязь'
        if other == 'Воздух':
            return 'Шторм'
        if other == 'Огонь':
            return 'Пар'
        if other == 'Вода':
            return 'Озеро'
        return other + self.element


class ElementAir:
    def __init__(self):
        self.element = 'Воздух'

    def __add__(self, other):
        if other == 'Земля':
            return 'Пыль'
        if other == 'Вода':
            return 'Шторм'
        if other == 'Огонь':
            return 'Молния'
        if other == 'Воздух':
            return 'Ветер'
        return other + self.element


class ElementFire:
    def __init__(self):
        self.element = 'Огонь'

    def __add__(self, other):
        if other == 'Земля':
            return 'Лава'
        if other == 'Воздух':
            return 'Молния'
        if other == 'Вода':
            return 'Пар'
        return other + self.element


earn = ElementEarn()
water = ElementWater()
fire = ElementFire()
air = ElementAir()

answer = water + air
print(answer)
answer = earn + fire
print(answer)
answer = earn + earn
print(answer)
answer = fire + air
print(answer)
#########################################################################
#24.7.PK
import random


class Human:

    def __init__(self, name):
        self.satiety = 50
        self.house = House()
        self.name = name

    def to_eat(self):
        self.house.refrigerator_with_food -= 5
        self.satiety += 5

    def work(self):
        self.satiety -= 5
        self.house.money += 10

    def play(self):
        self.satiety -= 5

    def visit_the_store(self):
        self.house.refrigerator_with_food += 10
        self.house.money -= 5

    def info(self):
        print(f'Человек по имени {self.name} имеет: \n'
              f'Сытость: {self.satiety}\n'
              f'Еды: {self.house.refrigerator_with_food}\n'
              f'Денег: {self.house.money}')


class House:

    def __init__(self):
        self.refrigerator_with_food = 50
        self.money = 0


man_vasya = Human('Вася')
man_nastya = Human('Настя')


def life(man):
    day = 0
    for day in range(366):
        number = random.randint(1, 6)
        if man.satiety < 20:
            if man.satiety < 0:
                print('\nЧеловек умер(\n')
                break
            man.to_eat()
        elif man.house.refrigerator_with_food < 20:
            man.visit_the_store()
        elif man.house.money < 50:
            man.work()
        elif number == 1:
            man.work()
        elif number == 2:
            man.to_eat()
        else:
            man.play()
    man.info()
    print(f'Прожил этот человек {day}\n')


life(man_vasya)
life(man_nastya)
#########################################################################
#24.8.PK
import random


class Card:
    def __init__(self):
        self.name_card = [
            'Двойка', 'Тройка', 'Четвёрка', 'Пятерка', 'Шестёрка',
            'Семёрка', 'Восьмерка', 'Девятка', 'Десятка', 'Валет',
            'Дама', 'Король', 'Туз'
        ]
        self.card_weight = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]


class Deck:
    def __init__(self):
        self.player = Card()

    def add_a_card(self):
        index_card = random.randint(0, 12)
        return self.player.name_card[index_card], self.player.card_weight[index_card]

    def play(self, person, computer):
        while True:
            if computer <= 19:
                print('Компьютер берет 1 карту')
                new_card = self.add_a_card()
                computer += new_card[1]
                continue
            if person <= 19:
                new_card = input('\nВзять карту? (да или нет): ').lower()
                if new_card == 'да':
                    new_card = self.add_a_card()
                    person += new_card[1]
                    print(f'Выпала тебе карта {new_card[0]} и теперь стало {person}\n')
                else:
                    return person, computer
            else:
                return person, computer


class Player:
    def __init__(self, name):
        self.name = name

    def info(self):
        deck = Deck()
        second_card = deck.add_a_card()
        first_card = deck.add_a_card()
        summ_card = second_card[1] + first_card[1]
        print(f'У Игрока {self.name} две карты: {second_card[0]} и {first_card[0]}')
        print(f'В сумме {summ_card} очков\n')
        return summ_card


man = Player('Вася')
bot = Player('Компьютер')

copy_person = man.info()
copy_bot = bot.info()
card = Deck()

player = card.play(copy_person, copy_bot)
person = player[0]
bot_1 = player[1]

while True:
    if bot_1 > 21:
        if person <= 21:
            print(f'У компьютера {bot_1} а у тебя {person} - Ты выйграл!')
    elif person > 21:
        if bot_1 <= 21:
            print(f'У компьютера {bot_1} а у тебя {person} - Компьютер выйграл!')
    elif person == bot_1 or bot_1 and person > 21 :
        print(f'У компьютера {bot_1} а у тебя {person} - Ничья')
    elif person == 21:
        print(f'У компьютера {bot_1} а у тебя {person} - Ты выйграл!')
    elif bot_1 == 21:
        print(f'У компьютера {bot_1} а у тебя {person} - Компьютер выйграл!')
    break
#########################################################################
#24.9.PK
class Cell:
    grid_cells = {
        1: ' ', 2: ' ', 3: ' ',
        4: ' ', 5: ' ', 6: ' ',
        7: ' ', 8: ' ', 9: ' '
    }

    def __init__(self, number_cell):
        self.number_cell = number_cell

    def checks_the_cell(self, cell_symbol):
        for key, value in Cell.grid_cells.items():
            if key == self.number_cell:
                if value == ' ':
                    Cell.grid_cells[self.number_cell] = cell_symbol
                    example_board = Board(cell_symbol)
                    example_board.info_result()
                else:
                    print('Клетка занята')


class Board:
    flag = False
    count = 0

    def __init__(self, cell_symbol):
        self.symbol = [cell_symbol for _ in range(3)]

    def info_result(self):
        Board.count += 1
        copy_cell = list(Cell.grid_cells.values())
        line_1 = copy_cell[:3]
        line_2 = copy_cell[3:6]
        line_3 = copy_cell[6:9]
        line_4 = copy_cell[0::4]
        line_5 = copy_cell[2:7:2]
        line_6 = copy_cell[2::3]
        line_7 = copy_cell[0::3]
        line_8 = copy_cell[1::3]
        print('\n', line_1, '\n', line_2, '\n', line_3)
        if line_1 == self.symbol or line_2 == self.symbol or line_3 == self.symbol or line_4 == self.symbol or \
                line_5 == self.symbol or line_6 == self.symbol or line_7 == self.symbol or line_8 == self.symbol:
            print('Победа!\n')
            Board.flag = True
        elif Board.count == 9:
            print('Ничья!\n')
            Board.flag = True


class Player:
    def __init__(self, name, cell_symbol):
        self.name = name
        self.cell_symbol = cell_symbol

    def cell_number(self, cell_number):
        print(f'{self.name} ходит на {cell_number} клетку')
        temp = Cell(cell_number)
        temp.checks_the_cell(self.cell_symbol)


print('Номера ячеек:')
print('[1 2 3]\n[4 5 6]\n[7 8 9]')
player_1 = Player('Алекс', 'X')
player_2 = Player('Ника', 'O')
while not Board.flag:
    choice = int(input('Введите номер ячейки: '))
    player_2.cell_number(choice)
    choice = int(input(f'Введите номер ячейки: '))
    player_1.cell_number(choice)
#########################################################################
#25.1.1
import math


class Circle:

    def __init__(self, x=0, y=0, r=1):
        self.set_x(x)
        self.set_y(y)
        self.__r = r

    def __str__(self):
        return f'x == {self.__x}, y == {self.__y} r == {self.__r}'

    def get_x(self):
        return self.__x

    def set_x(self, x):
        if isinstance(x, int):
            self.__x = x
        else:
            raise Exception('Х должен быть числом')

    def get_y(self):
        return self.__y

    def set_y(self, y):
        if isinstance(y, int):
            self.__y = y
        else:
            raise Exception('Y должен быть числом')

    def perimeter(self):
        answer_perimeter = 2 * math.pi * self.__r
        print(answer_perimeter)

    def square(self):
        answer_square = math.pi * self.__r ** 2
        print(answer_square)

    def increase_scale(self, k):
        self.__r *= k
        print(self.__r)

    def is_intersect(self, other):
        print((self.__x - other.__x) ** 2 + (self.__y - other.__y) ** 2 <= (self.__r + other.__r) ** 2)


first_data = Circle(0, 0, 1)
print(first_data) # str+
first_data.perimeter()
first_data.square()
first_data.increase_scale(2)
print(first_data.get_x())
print(first_data.get_y())
second_data = Circle(1, 3, 2)
first_data.is_intersect(second_data)
#########################################################################
#25.1.2
class Person:
    __count = 0

    def __init__(self, name, age):
        self.__name = ''
        self.__age = 0
        self.set_age(age)
        self.set_name(name)
        Person.__count += 1

    def __str__(self):
        return f'Имя: {self.__name}, возраст: {self.__age}'

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age in range(0, 100):
            self.__age = age
        else:
            raise Exception('Такого возраста не существует')

    def set_name(self, name):
        if isinstance(name, str) and name.isalpha():
            self.__name = name
        else:
            raise Exception('Имя должно быть без цифр и быть строкой')


man = Person('Коля', 23)
man_2 = Person('Вася', 14)
man.set_name('Николай')
man.set_age(35)
print(man)
print(Person._Person__count) # Несмотря на выделенный цвет он выводит инфу - но так делать не стоит
#########################################################################
#25.2.1
class Ship:
    __count_ships = 0

    def __init__(self, model):
        self.__model = model
        Ship.__count_ships += 1

    def __str__(self):
        return f'Корабль {self.__model} с номером {Ship.__count_ships}'

    def sail(self):
        print(f'Корабль {self.__model} пошёл по воде')


class CargoShip(Ship):

    def __init__(self, model, fullness=0):
        super().__init__(model)
        self.fullness = fullness

    def load(self):
        self.fullness += 1
        print(f'Загруженность {self.fullness}')

    def upload(self):
        if self.fullness > 0:
            self.fullness -= 1
            print(f'Загруженность {self.fullness}')
        else:
            raise Exception('Корабль уже разгружен')


class Warship(Ship):

    def __init__(self, model, weapon):
        super().__init__(model)
        self.weapon = weapon

    def attack(self):
        print(f'Корабль стреляет из {self.weapon}')


a = Warship('tr33', 'пушка')
print(a)
a.attack()
a.sail()
b = CargoShip('admiral')
b.load()
b.upload()
#########################################################################
#25.2.2
class Robot:
    __countRobot = 0

    def __init__(self, model):
        self.model = model
        Robot.__countRobot += 1

    def operate(self):
        print('Пылесос поехал по кругу')


class RobotCleaner(Robot):

    def __init__(self, model, rubbish=0):
        super().__init__(model)
        self.rubbish = rubbish

    def operate(self):
        self.rubbish += 1
        print(f'Робот пылесос {self.model}, заполненность мешка - {self.rubbish}')


class MilitaryRobot(Robot):

    def __init__(self, model, weapon):
        super().__init__(model)
        self.weapon = weapon

    def operate(self):
        print(f'я {self.model}, приступаю защищать военный объект с помощью {self.weapon}')


class RobotSubmarine(MilitaryRobot):

    def __init__(self, model, weapon, depth):
        super().__init__(model, weapon)
        self.depth = depth

    def operate(self):
        super().operate()
        print(f'Охрана роботом {self.model} ведётся под водой на глубине {self.depth}')


a = RobotCleaner('Домашний')
a.operate()
b = MilitaryRobot('Сибирь', 'Кинжал')
b.operate()
c = RobotSubmarine('Akula', 'Сатана', 3)
c.operate()
#########################################################################
#25.2.3
class DivisionError(Exception):
    pass


file = open('number.txt', 'r', encoding='utf8')
for line in file:
    a = line.split() # a rstrip удаляет на конце лишние символы
    answer = int(a[0]) / int(a[1])
    print(f'{a[0]} : {a[1]} = {answer}')
    if int(a[0]) < int(a[1]):
        raise DivisionError('Нельзя делить меньшее на большее')

#########################################################################
#25.3
class Unit:

    def __init__(self, hp, damag=0):
        self.hp = hp
        self.damag = damag

    def damage(self):
        self.hp -= 0


class Soldier(Unit):

    def __init__(self, hp, damag):
        super().__init__(hp, damag)

    def __str__(self):
        return f'У Солдата {self.hp} ХП урон по нему составил {self.damage()}'

    def damage(self):
        self.hp -= self.damag
        return self.hp


class Citizen(Unit):
    def __init__(self, hp, damag):
        super().__init__(hp, damag)

    def __str__(self):
        return f'У Гражданского {self.hp} ХП урон по нему составил {self.damage()}'

    def damage(self):
        self.damag *= 2
        self.hp -= self.damag
        return self.hp


a = Soldier(hp=200, damag=20)
print(a)
b = Citizen(hp=300, damag=15)
print(b)
#########################################################################
#25.3(моё выше - а это наставника)
class Unit:

    def __init__(self, hp):
        self.__hp = hp

    def set_hp(self, amount):
        self.__hp = amount

    def get_hp(self):
        return self.__hp

    def get_damage(self, amount):
        self.set_hp(self.get_hp() - 0)  # -0 написан для наглядности, в теории мы могли бы этого и не писать


class Soldier(Unit):

    def get_damage(self, amount):
        self.set_hp(self.get_hp() - amount)


class Citizen(Unit):
    def get_damage(self, amount):
        self.set_hp(self.get_hp() - amount * 2)

#########################################################################
#25.4
class CanFly:

    def __init__(self):
        self.height = 0
        self.speed = 0

    def fly_up(self):
        pass

    def fly(self):
        pass

    def land(self):
        self.height = 0
        self.speed = 0

    def __str__(self):
        return f'Находится на высоте: {self.height}, и данная скорость: {self.speed}'


class Butterfly(CanFly):

    def fly_up(self):
        self.height = 1

    def fly(self):
        self.speed = 0.5


class Rocket(CanFly):

    def fly_up(self):
        self.height = 500
        self.speed = 1000

    def land(self):
        self.height = 0
        print('БА-БАХ!')

    def explode(self):
        pass
#########################################################################
#25.PK 1

class Property:
    """
    Базовый класс - характеризующий собственность,

    __worth: собственный капитал
    """
    __worth = 0

    def designer(self, price):
        """
        Конструктор для высчитывания налога с собственного капитала.

        :param price: приходящий подсчитанный налог.
        :type price: int
        """
        print(f'\nБаланс вашего счёта: {Property.__worth} руб')
        print(f'Налог составит: {price} руб.')
        Property.__worth -= price
        if Property.__worth < 0:
            print(f'!!Вам необходимо набрать {abs(Property.__worth)} руб. для оплаты налога!!')

    def set_worth(self, capital):
        """
        Сеттер для установления собственного капитала

        :param capital: собственный капитал
        :type capital: int
        :raise Exception: Если собственного капитала меньше ноля, то вызывается исключение
        """
        if capital > 0:
            Property.__worth = capital
        else:
            raise Exception('На вашем счету недостаточно средств, для оплаты налога!')


class Apartment(Property):
    """
    Класс Квартира. Родитель Property

    :arg
        tax_calculation(int) - передаётся стоимость квартиры
    """
    def __init__(self, price_apartament):
        self.tax_calculation(price_apartament)
    """
    метод tax_calculation() - Считает налог на квартиру
    и передает значение в designer(Конструктор) родительского класса
    :arg
        :type price_apartament : int
    :return: передает подсчитанный налог в designer(Конструктор) родительского класса 
    """
    def tax_calculation(self, price_apartament):
        price_apartament /= 1000
        return super().designer(price_apartament)


class Car(Property):
    """
    Класс Машина. Родитель Property

    :arg
        tax_calculation(int) - передаётся стоимость машины
    """
    def __init__(self, price_car):
        self.tax_calculation(price_car)
    """
    метод tax_calculation() - Считает налог на машину
    и передает значение в designer(Конструктор) родительского класса
    :arg
        :type price_car : int
    :return: передает подсчитанный налог в designer(Конструктор) родительского класса 
    """
    def tax_calculation(self, price_car):
        price_car /= 200
        return super().designer(price_car)


class CountryHouse(Property):
    """
    Класс Дача. Родитель Property

    :arg
        tax_calculation(int) - передаётся стоимость дачи
    """
    def __init__(self, price_country_house):
        self.tax_calculation(price_country_house)

    """
    метод tax_calculation() - Считает налог на дачу
    и передает значение в designer(Конструктор) родительского класса
    :arg
        :type price_country_house : int
    :return: передает подсчитанный налог в designer(Конструктор) родительского класса 
    """
    def tax_calculation(self, price_country_house):
        price_country_house /= 500
        return super().designer(price_country_house)


money = int(input('Введите количество ваших денег: '))
value_apartament = int(input('Введите стоимость вашей квартиры: '))
value_car = int(input('Введите стоимость вашего автомобиля: '))
value_country_house = int(input('Введите стоимость вашей дачи: '))


my_money = Property()
my_money.set_worth(money)
my_first_property = Apartment(price_apartament=value_apartament)
my_second_property = Car(price_car=value_car)
my_third_property = CountryHouse(price_country_house=value_country_house)
#########################################################################
#25.PK 2
# Импортируем модуль для генерации случайных чисел
import random


# Создаем классы исключений
class KillError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


# Создаем функцию, которая возвращает количество кармы от 1 до 7 и может выкинуть исключение с вероятностью 1 к 10
def analyzes_the_day():
    # Генерируем случайное число от 1 до 10
    exception_probability_number = random.randint(1, 10)
    # Если число равно 1, то выбрасываем одно из исключений
    if exception_probability_number == 1:
        # Создаем список из классов исключений
        errors = [KillError, DrunkError, CarCrashError, GluttonyError, DepressionError]
        # Выбираем случайный класс из списка
        error = random.choice(errors)
        # Выбрасываем исключение этого класса
        raise error()
    # Иначе возвращаем случайное число от 1 до 7 как количество кармы
    else:
        return random.randint(1, 7)


# Создаем константу для уровня кармы, необходимого для просветления
ENLIGHTENMENT = 500
# Создаем переменную для хранения текущего уровня кармы
karma = 0
# Открываем файл для записи логов об исключениях
log_file = open('karma.log', 'w')

# Создаем бесконечный цикл по набору кармы
while True:
    # Пытаемся вызвать функцию analyzes_the_day() и прибавить ее результат к текущему уровню кармы
    try:
        karma += analyzes_the_day()
        print(f'Текущий уровень кармы: {karma}')
    # Ловим исключения разных классов и записываем их в файл с помощью метода write()
    except KillError:
        log_file.write('KillError\n')
        print('Вы убили живое существо!')
    except DrunkError:
        log_file.write('DrunkError\n')
        print('Вы напились!')
    except CarCrashError:
        log_file.write('CarCrashError\n')
        print('Вы попали в аварию!')
    except GluttonyError:
        log_file.write('GluttonyError\n')
        print('Вы объелись!')
    except DepressionError:
        log_file.write('DepressionError\n')
        print('Вы впали в депрессию!')

    # Проверяем, достиг ли текущий уровень кармы необходимого для просветления значения константы ENLIGHTENMENT
    if karma >= ENLIGHTENMENT:
        # Если да, то выводим сообщение о просветлении и выходим из цикла с помощью оператора break
        print(f'Поздравляем! Вы достигли просветления с уровнем кармы {karma}!')
        break

# Закрываем файл после выхода из цикла с помощью метода close()
log_file.close()
#########################################################################
#25.PK 3
class MyDict(dict):
    """
    Класс МойСловарь. Родитель: dict
    """
    def get(self, key, default=None):
        """
            Метод, который ищет значение от ключа (key) в словаре.
        :param key: передается ключ из словаря.
        :param default: значение, которое возвращается если нет искомого ключа в словаре.
        :return: возвращаем через родительский класс (dict) значение от ключа(key), но если его нет,
        возвращаем default которому мы присвоили значение '0'
        """
        return super(MyDict, self).get(key, 0)


b = MyDict({1: 'Gt', 2: 'rs'})
print(b.get(key=1))
print(b.get(key=3))
#########################################################################
#25.PK 4(1)
import random


class Hero:
    # Базовый класс, который не подлежит изменению
    # У каждого наследника будут атрибуты:
    # - Имя
    # - Здоровье
    # - Сила
    # - Жив ли объект
    # Каждый наследник будет уметь:
    # - Атаковать
    # - Получать урон
    # - Выбирать действие для выполнения
    # - Описывать своё состояние
    max_hp = 150
    start_power = 10

    def __init__(self, name):
        self.name = name
        self.__hp = self.max_hp
        self.__power = self.start_power
        self.__is_alive = True

    def get_hp(self):
        return self.__hp

    def set_hp(self, new_value):
        self.__hp = max(new_value, 0)

    def get_power(self):
        return self.__power

    def set_power(self, new_power):
        self.__power = new_power

    def is_alive(self):
        return self.__is_alive

    # Все наследники должны будут переопределять каждый метод базового класса (кроме геттеров/сеттеров)
    # Переопределенные методы должны вызывать методы базового класса (при помощи super).
    # Методы attack и str базового класса можно не вызывать (т.к. в них нету кода).
    # Они нужны исключительно для наглядности.
    # Метод make_a_move базового класса могут вызывать только герои, не монстры.    def attack(self, target):
        # Каждый наследник будет наносить урон согласно правилам своего класса
    def take_damage(self, damage):
        # Каждый наследник будет получать урон согласно правилам своего класса
        # При этом у всех наследников есть общая логика, которая определяет жив ли объект.
        print("\t", self.name, "Получил удар с силой равной = ", round(damage),
              ". Осталось здоровья - ", round(self.get_hp()))
        # Дополнительные принты помогут вам внимательнее следить за боем и изменять стратегию,
        # чтобы улучшить выживаемость героев
        if self.get_hp() <= 0:
            self.__is_alive = False

    def make_a_move(self, friends, enemies):
        # С каждым днём герои становятся всё сильнее.
        self.set_power(self.get_power() + 0.1)

    def __str__(self):
        return 'Name: {0} | HP: {1}'.format(self.name, self.get_hp())


class Healer(Hero):
    # Целитель:
    # Атрибуты:
    def __init__(self, name):
        super().__init__(name)
        self.magic_power = self.get_power() * 3
    # - магическая сила - равна значению НАЧАЛЬНОГО показателя силы умноженному на 3 (self.__power * 3)
    # Методы:

    def attack(self, target):
        target.take_damage(self.get_power() / 2)
        # - атака - может атаковать врага, но атакует только в половину силы self.__power

    def take_damage(self, damage):
        self.set_hp(self.get_hp() - (1.2 * damage))
        super().take_damage(damage)
    # - получение урона - т.к. защита целителя слаба - он получает на 20% больше урона (1.2 * damage)

    def healing(self, target):
        target.set_hp(target.get_hp() + self.magic_power)
    # - исцеление - увеличивает здоровье цели на величину равную своей магической силе

    def make_a_move(self, friends, enemies):
        print(self.name, end=' ')
        target_of_potion = friends[0]
        min_health = target_of_potion.get_hp()
        for friend in friends:
            if friend.get_hp() < min_health:
                target_of_potion = friend
                min_health = target_of_potion.get_hp()
        if min_health < 130 and self.magic_power > 0:
            print("Исцеляю", target_of_potion.name)
            self.healing(target_of_potion)
        else:
            if not enemies:
                return
            print("Атакую ближнего -", enemies[0].name)
            self.attack(enemies[0])
            print('\n')
        # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии
        # выполняет ОДНО из действий (атака,    # исцеление) на выбранную им цель


class Tank(Hero):
    # Танк:
    # Атрибуты:
    def __init__(self, name):
        super().__init__(name)
        self.defense = 1
        self.shield = False
        # - показатель защиты - изначально равен 1, может увеличиваться и уменьшаться
        # - поднят ли щит - танк может поднимать щит, этот атрибут должен показывать поднят ли щит в данный момент
    # Методы:

    def attack(self, target):
        target.take_damage(self.get_power() / 2)
        # - атака - атакует, но т.к. доспехи очень тяжелые - наносит половину урона (self.__power)

    def take_damage(self, damage):
        self.set_hp(self.get_hp() - (damage / self.defense))
        super().take_damage(damage)
    # - получение урона - весь входящий урон делится на показатель защиты (damage/self.defense) и
    # только потом отнимается от здоровья

    def shield_up(self):
        self.shield = True
        print('Поднимаю щит')
        self.defense *= 2
        self.set_power(self.get_power() / 2)

    def shield_down(self):
        self.shield = False
        print('Опускаю щит')
        self.defense /= 2
        self.set_power(self.get_power() * 2)
    # - поднять щит - если щит не поднят - поднимает щит. Это увеличивает показатель брони в 2 раза, но
    # уменьшает показатель силы в 2 раза.
    # - опустить щит - если щит поднят - опускает щит. Это уменьшает показатель брони в 2 раза, но увеличивает
    # показатель силы в 2 раза.

    def make_a_move(self, friends, enemies):
        print(self.name, end=' ')
        if not enemies:
            return
        if self.defense > 2:
            self.shield_down()
        else:
            print("Атакую без щита -", enemies[0].name)
            self.attack(enemies[0])
            self.shield_up()
        print('\n')
        # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет
        # ОДНО из действий (атака,
        # поднять щит/опустить щит) на выбранную им цель


class Attacker(Hero):
    # Убийца:
    # Атрибуты:
    def __init__(self, name):
        super().__init__(name)
        self.power_multiply = 1
    # - коэффициент усиления урона (входящего и исходящего)

    def get_power_multiply(self):
        return round(self.power_multiply, 2)

    def set_power_multiply(self, new_power):
        self.power_multiply = round(new_power, 2)

    # Методы:
    def attack(self, target):
        target.take_damage(self.get_power() * self.power_multiply)
        self.power_down()
        # - атака - наносит урон равный показателю силы (self.__power)
        # умноженному на коэффициент усиления урона (self.power_multiply)
        # после нанесения урона - вызывается метод ослабления power_down.

    def take_damage(self, damage):
        self.set_hp(self.get_hp() - (damage * self.power_multiply / 2))
        super().take_damage(damage)
    # - получение урона - получает урон равный входящему урона умноженному на половину коэффициента усиления урона -
    # damage * (self.power_multiply / 2)

    def power_up(self):
        self.set_power_multiply(self.power_multiply * 2)
        # - усиление (power_up) - увеличивает коэффициента усиления урона в 2 раза

    def power_down(self):
        self.set_power_multiply(self.power_multiply / 2)
        # - ослабление (power_down) - уменьшает коэффициента усиления урона в 2 раза

    def make_a_move(self, friends, enemies):
        print(self.name, end=' ')
        target = random.choice(enemies)
        if self.get_power_multiply() < 2:
            print('Баф на усиление Атаки')
            self.power_up()
        else:
            print("Атака!!! Уровень урона - " + str(self.get_power()) + " Случайно атакую -", target.name)
            print()
            self.attack(target)
        if not enemies:
            return
        print('\n')
        # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей
        # стратегии выполняет ОДНО из действий (атака,
        # усиление, ослабление) на выбранную им цель
#########################################################################
#25.PK 4(2)
import random
#from monsters import MonsterBerserk, MonsterHunter СнЯТЬ решетки
#from heroes import Tank, Healer, Attacker


def one_year_of_war():
    # Ниже приведен пример составления команды
    # Вы можете изменять состав команды, НО размер команды не должен быть более 5.

    tank = Tank("Танк Пётр")
    attacker = Attacker("Убийца Ольга")
    second_attacker = Attacker("Убийца Траур")
    healer = Healer("Монах Игнат")
    second_healer = Healer("Монах Ирэна")
    good_team = [tank, attacker, second_attacker, second_healer, healer]

    # Код ниже изменять нельзя!

    # Функция запускает симуляцию одного года сражений.
    # В цикле запускается 365 итераций (1 итерация = 1 день)
    # Каждый день каждый герой и монстр выбирают и совершают ОДНО действие.
    # Если монстры умирают - они пропадают из списка
    # Если умирают герои - цикл завершается - битва считается проигранной (возвращается 0)
    # Если герои выживают - битва считается выигранной (возвращается 1)
    if sum([isinstance(hero, (MonsterHunter, MonsterBerserk)) for hero in good_team]) > 1:
        print("В команде героев может быть только 1 монстр!")
        return 0

    evil_names = ["Абвыргл", "Мефисто", "Драник", "Диабло", "Пусечка", "Стаут"]
    mob_warrior = MonsterBerserk("Берсерк " + random.choice(evil_names))
    mob_ranger = MonsterHunter("Рейнджер " + random.choice(evil_names))
    evil_team = [mob_warrior, mob_ranger]

    for day in range(1, 366):
        print("=" * 50 + "\nНачало дня №" + str(day) + "\n" + "=" * 50)

        # В циклах у героев и монстров вызывается метод make_a_move, который должен выбирать и совершать одно действие
        # Для наглядности вы можете добавлять в каждое действие принты с подробностями (чтобы знать кто когда и что совершает)
        # При помощи этой информации вы сможете искать проблемы и ошибки в вашем коде и в конечном итоге это поможет вам улучшить стратегию
        print("\nКоманда добра:\n" + '-' * 50)
        for hero in good_team:
            hero.make_a_move(good_team, evil_team)

        print("\nКоманда зла:\n" + '-' * 50)
        for mob in evil_team:
            mob.make_a_move(evil_team, good_team)

        print(f"Итоги дня сражений №{day}")

        # В итогах дня у каждого героя и каждого монстра вызывается метод __str__ который должен описывать их текущее состояние
        print("\nКоманда добра:\n" + '-' * 50)
        for hero in good_team:
            print(hero)

        print("\nКоманда зла:\n" + '-' * 50)
        for mob in evil_team:
            print(mob)

        # Мёртвые монстры удаляются из списка
        evil_team = [mob for mob in evil_team if mob.is_alive()]
        # Новые монстры в чётные дни добавляются в список (но их не может быть больше 4)
        if day % 2 == 0 and len(evil_team) < 4:
            newborn_evils = [MonsterBerserk("Берсерк " + random.choice(evil_names)), MonsterHunter("Рейнджер " + random.choice(evil_names))]
            evil_team.append(random.choice(newborn_evils))

        if any([not hero.is_alive() for hero in good_team]):
            print("Вы проиграли!")
            return 0
        else:
            print("Сражение продолжается!")

    else:
        print("Вы одержали победу!")
        return 1


# Код ниже не подлежит изменению
# Он запускает 20 симуляций. Для зачёта по заданию вам надо стабильно набирать 10 или более побед.
count_of_wins = 0
for year in range(1, 21):
    count_of_wins += one_year_of_war()

print("Из 20 раз команда героев одержала", count_of_wins, "побед")
if count_of_wins < 10:
    print("Героям нужна другая тактика, попробуйте ещё!")
else:
    print("Герои готовы к реальному сражению, задание выполнено!")

#########################################################################
#25.PK 4(3)
import random


class Monster:
    max_hp = 150
    start_power = 10

    def __init__(self, name):
        self.name = name
        self.__hp = self.max_hp
        self.__power = self.start_power
        self.__is_alive = True

    def get_hp(self):
        return self.__hp

    def set_hp(self, new_value):
        self.__hp = max(new_value, 0)

    def get_power(self):
        return self.__power

    def set_power(self, new_power):
        self.__power = new_power

    def attack(self, target):
        pass

    def is_alive(self):
        return self.__is_alive

    def take_damage(self, damage):
        print("\t", self.name, "Получил удар с силой равной = ", round(damage), ". Осталось здоровья - ", round(self.get_hp()))
        if self.get_hp() <= 0:
            self.__is_alive = False

    def make_a_move(self, friends, enemies):
        pass

    def __str__(self):
        return 'Name: {0} | HP: {1}'.format(self.name, self.get_hp())


class MonsterBerserk(Monster):

    def __init__(self, name):
        super().__init__(name)
        self.madness = 1

    def attack(self, target):
        target.take_damage(self.get_power() * self.madness)
        self.madness += 0.1

    def take_damage(self, power):
        self.set_hp(self.get_hp() - power * (self.madness / 2))
        if self.get_hp() < 50:
            self.madness *= 2
        super().take_damage(power)

    def make_a_move(self, friends, enemies):
        print(self.name, end=' ')
        self.madness = min(self.madness, 4)
        if not enemies:
            return
        if self.madness < 3:
            print("Атакую того, кто стоит ближе -", enemies[0].name)
            self.attack(enemies[0])
        else:
            target = random.choice(enemies)
            print("BERSERK MODE!!! Уровень безумия - " + str(self.madness) + " Случайно атакую -", target.name)
            print()
            self.attack(target)
        print('\n')


class MonsterHunter(Monster):

    def __init__(self, name):
        super().__init__(name)
        self.potions = 10

    def attack(self, target):
        target.take_damage(self.get_power() + (10 - self.potions))

    def take_damage(self, power):
        self.set_hp(self.get_hp() - power)
        if random.randint(1, 10) == 1:
            self.potions -= 1
        super().take_damage(power)

    def give_a_potion(self, target):
        self.potions -= 1
        target.set_hp(target.get_hp() + self.get_power())

    def make_a_move(self, friends, enemies):
        print(self.name, end=' ')
        target_of_potion = friends[0]
        min_health = target_of_potion.get_hp()
        for friend in friends:
            if friend.get_hp() < min_health:
                target_of_potion = friend
                min_health = target_of_potion.get_hp()

        if min_health < 60 and self.potions > 0:
            print("Исцеляю", target_of_potion.name)
            self.give_a_potion(target_of_potion)
        else:
            if not enemies:
                return
            print("Атакую ближнего -", enemies[0].name)
            self.attack(enemies[0])
        print('\n')

#########################################################################
#25.PK 5
class Stack:
    """
    Класс Стэк.

    Attributes:

        __new_roster (List) - Список
    """

    def __init__(self):
        self.__new_roster = []

    def __str__(self):
        return '; '.join(self.__new_roster)

    """
        Метод __str__ возвращает (принтует в консоль) задачи через "точку с запятой" 
    """

    def push(self, elem):
        self.__new_roster.append(elem)

    """
        Метод Пуш добавляет в список new_roster входящие задачи

        Arg:
         elem (str) - передается номер и задача
    """

    def pop(self):
        if len(self.__new_roster) == 0:
            return None
        return self.__new_roster.pop()

    """
        Метод Pop удаляет последний элемент из списка, но если список пуст, возвращает None
    """


class TaskManager:
    """
    Класс Менеджер Задач.

    Attributes:
        roster (dict) - Словарь
    """

    def __init__(self):
        self.roster = dict()

    def __str__(self):
        display = []
        if self.roster:
            for i_number in sorted(self.roster.keys()):
                display.append(f'{str(i_number)} {self.roster[i_number]}\n')
            return ''.join(display)
        """
            Метод __str__ возвращает и принтует новый список
        """

    def new_task(self, task: str, number_task: int):
        if number_task not in self.roster:
            self.roster[number_task] = Stack()
        self.roster[number_task].push(task)
        """
            Метод new_task проверяет есть ли такой номер в реестре,
            если нет, то вызывает Класс Стэк,
            иначе добавляет через метод Пуш новую задачу

            arg:
                task (str) - передается задача
                number_task (int) - передается номер задачи(приоритет)
        """


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать ДЗ", 2)
print(manager)
#########################################################################
#26.PK 1

f = [1, 2, 3] # - создаем итрерируемый объект
e = f.__iter__() # или e = iter(f) - создаем итератор
print(e.__next__()) # Выдает 1
print(e.__next__()) # Выдает 2
print(next(e)) # или так и последовательно Выдает 3
# Если попытаемся вывести следующий то будет ошибка-итератор одноразовый


roster = [1, 2, 3, 4, 5]
iter_roster = iter(roster)
while iter_roster:
    try:
        print(next(iter_roster))
    except StopIteration:
        print('Конец!')
        break


class CountIterator:
    count = 0
    def __iter__(self):
        return self
    def __next__(self):
        CountIterator.count += 1
        return CountIterator.count

my_iter = CountIterator()
for i_elem in my_iter:
    print(i_elem)

#########################################################################
#26.PK 2 #13.4.2
import random


class CountIterator:
    count = 0

    def __init__(self, count_number):
        self.count_number = count_number

    def __iter__(self):
        return self

    def __next__(self):
        if self.count_number > 0:
            CountIterator.count += random.uniform(0.0, 1.0)
            self.count_number -= 1
            return round(CountIterator.count, 2)
        raise StopIteration


limit = int(input('Кол-во элементов: '))
my_iter = CountIterator(limit)
print('Элементы итератора:')
for i_elem in my_iter:
    print(i_elem)

#########################################################################
#14.2.1
from typing import Callable

def func_2(my_func: Callable, *args, **kwargs) -> int:
    return my_func(*args, **kwargs) * my_func(*args, **kwargs)

def func_1(x: int) -> int:
    return x + 10

print(func_2(func_1, 9))
#########################################################################
#14.2.2
from typing import Callable, Any
import time


def timer(my_func: Callable, *args, **kwargs) -> Any:
    """Функция - таймер. Выводит время работы функции и возвращает её результат"""
    started_at = time.time()
    result = my_func(*args, **kwargs)
    end_at = time.time()
    answer_at = round(end_at - started_at, 4)
    print(f'Функция работала: {answer_at} секунд(ы)')

    return result


def squares_sum() -> int:
    number = 100
    result = 0
    for _ in range(number + 1):
        result += sum([i_num**2 for i_num in range(10000)])

    return result


def cube_sum(number: int) -> int:
    result = 0
    for _ in range(number + 1):
        result += sum([i_num**3 for i_num in range(10000)])

    return result


my_result = timer(squares_sum)
print(my_result)
my_result_cube = timer(cube_sum, 200)
print(my_result_cube)
#########################################################################
#14.3.1
from typing import Callable, Any


def do_twice(func: Callable) -> Callable:
    """
    Декоратор do_twice,
    который дважды вызывает декорируемую функцию.
    """

    def wrapped_greeting(*args, **kwargs) -> Any:
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapped_greeting


@do_twice
def greeting(name: str) -> Any:
    print('Привет, {name}!'.format(name=name))


greeting('Tom')
#########################################################################
#14.3.2
import time
from typing import Callable, Any


def timer(my_func: Callable) -> Any:
    """
    Декоратор, выводящий время, которое заняло
    выполнение декорируемой функции.
    """
    def wrapped_func(*args, **kwargs):
        started_at = time.time()
        result = my_func(*args, **kwargs)
        end_at = time.time()
        answer_at = round(end_at - started_at, 4)
        print(f'Функция работала: {answer_at} секунд(ы)')
        return result
    return wrapped_func


@timer
def squares_sum() -> int:
    number = 100
    result = 0
    for _ in range(number + 1):
        result += sum([i_num**2 for i_num in range(10000)])
    return result


@timer
def cube_sum(number: int) -> int:
    result = 0
    for _ in range(number + 1):
        result += sum([i_num**3 for i_num in range(10000)])
    return result


a = cube_sum(200)
print(a)
b = squares_sum()
print(b)
#########################################################################
# 14.4
from typing import Callable, Any


def bread(func: Callable) -> Callable:
    """
    Декоратор bread, который складывает сэндвича
    """

    def wrapped_bread(*args, **kwargs) -> Any:
        print('</ ----------\>')
        func(*args, **kwargs)
        print('<\______/>')

    return wrapped_bread


def ingredients(func: Callable) -> Callable:
    """
    Декоратор indigrients, которые входят в состав сэндвича
    """

    def wrapped_bread(name, name_2, name_3) -> Any:
        print('#{name}#\n--{name_2}--\n~{name_3}~'.format(name=name, name_2=name_2, name_3=name_3))
        return func(name, name_2, name_3)

    return wrapped_bread


@bread
@ingredients
def sandwich(name: str, name_2: str, name_3: str) -> Any:
    return sandwich


sandwich('помидоры', 'ветчина', 'салат')

#########################################################################
# 14.4.2
from typing import Callable

plugins = dict()


def decorator(func: Callable) -> Callable:
    plugins[func.__name__] = func
    return func


@decorator
def say():    print('hi!')


print(plugins)
#########################################################################
#PK 14.1

from typing import Callable
import functools

def how_are_you(func: Callable) -> Callable:
    """
    Декоратор how_are_you. Спрашивает "как дела?" и отвечает.
    """
    @functools.wraps(func)
    def wrapped_question() -> Any:
        _ = input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        return func()
    return wrapped_question


@how_are_you
def test():
    print('<Тут что-то происходит...>')


test()
print(how_are_you.__doc__)
#########################################################################
#PK 14.2
from typing import Callable, Any
import functools
import threading


def timer(my_func: Callable) -> Any:
    """
   Декоратор timer, выводит функцию header, каждые 5 секунд.
    """
    @functools.wraps(my_func)
    def wrapped_func(*args, **kwargs):
        threading.Timer(5.0, header).start()
        my_func(*args, **kwargs)
        return my_func
    return wrapped_func


@timer
def header() -> Any:
    print('Title, html')


print(timer.__doc__)
header()
#########################################################################
#PK 14.3
from typing import Callable, Any
import functools
import datetime


def logging(func: Callable) -> Any:
    """
    Декоратор logging, отвечает за логирование функций.
    """
    print(func.__doc__)

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        file = open('function_errors.log', 'a', encoding='utf-8')
        temp = func(*args, **kwargs)
        datetime_now = datetime.datetime.now()
        file.write('\nФункция - {func}, Ошибка! - {temp}, Время: {datetime_now}\n'.format(func=func.__name__,
                                                                                          temp=str(temp),
                                                                                          datetime_now=datetime_now))
        file.close()
        return temp
    return wrapped_func


@logging
def division() -> Any:
    """
    Функция division, Делит 2 числа
    """
    try:
        answer = 8 / 0
    except BaseException as answer:
        return answer


@logging
def folding() -> Any:
    """
    Функция folding, складывает 2 числа
    """
    try:
        answer = 5 + '4'
    except BaseException as answer:
        return answer


division()
folding()

#########################################################################
#PK 14.4
from typing import Callable, Any
import functools


def counter(func: Callable) -> Any:
    """
    Декоратор counter, cчитает кол-во вызовов обертки декоратора.
   """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        counter.count += 1
        temp = func(*args, **kwargs)
        print(f'Функция {func.__name__} вызвана: {counter.count} раз')
        return temp
    counter.count = 0
    return wrapped_func

@counter
def test() -> Any:
    print('test')

test()
test()
#########################################################################
#15
from abc import ABC, abstractmethod


class Figure(ABC):
    """
    Абстрактный класс Фигура
    """

    def __init__(self, pos_x: int, pos_y: int, length: int, width: int) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.length = length
        self.width = width

    @abstractmethod
    def move(self, pos_x: int, pos_y: int) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y


class ResizableMixin:
    def resize(self, length: int, width: int) -> None:
        self.length = length
        self.width = width


class Rectangle(Figure, ResizableMixin):
    """
    Прямоугольник
    """

    def move(self, pos_x: int, pos_y: int) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y


class Square(Figure, ResizableMixin):
    """ Квадрат """

    def __init__(self, pos_x: int, pos_y: int, size: int) -> None:
        super().__init__(pos_x, pos_y, size, size)

    def move(self, pos_x: int, pos_y: int) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y




rect_1 = Rectangle(pos_x=10, pos_y=20, length=5, width=6)
rect_2 = Rectangle(pos_x=30, pos_y=40, length=10, width=11)
square_1 = Square(pos_x=50, pos_y=70, size=7)


for figure in [rect_1, rect_2, square_1]:
    new_size_x = figure.length * 2
    new_size_y = figure.width * 2
    figure.resize(new_size_x, new_size_y)


test = Square(1, 2, 34)
print(Square.__name__)

#############################################################
from abc import ABC, abstractmethod


class MusicMixin:

    def music(self):
        print('Я свободен! Словно птица в небесах')


class Transport(ABC):

    @abstractmethod
    def ride_earth(self):
        pass

    @abstractmethod
    def ride_water(self):
        pass


class Auto(Transport):

    def ride_earth(self):
        print('Я еду по земле')


class Boat(Transport):

    def ride_water(self):
        print('Я еду по воде')


class Amphibians(Auto, Boat, MusicMixin):
    pass


a = Amphibians()
a.music()
a.ride_earth()
a.ride_water()

#############################################################
#Контекст менеджер

class File:
    def __init__(self, filename, mode) -> None:
        print('Открывание файла')
        self.filename = filename
        self.mode = mode
        self.start = None

    def __enter__(self) -> 'File':
        self.start = open(self.filename, self.mode, encoding='utf-8')
        return self.start

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.start.close()
        return True


with File('example.txt', 'w') as file:
    file.write('Всем привет!')

#############################################################
class Example:
    def __init__(self) -> None:
        print('Вызов __init__')

    def __enter__(self) -> 'Example':
        self.a = 'Вызов __enter__'
        print(self.a)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Вызов __exit__')
        if exc_type is Exception:
            return True


my_obj = Example()

with my_obj as obj:
    print('Код внутри первого вызова контекст менеджера')

    with my_obj as obj2:
        raise Exception('Выброс исключения во вложенном (втором) вызове контекст менеджере')

    print('Я обязательно выведусь...')
#############################################################
from abc import ABC, abstractmethod


class MusicMixin:

    def music(self):
        print('Я свободен! Словно птица в небесах')


class Transport(ABC):
    def __init__(self, color: str, speed: int) -> None:
        self._color = color
        self._speed = speed

    def __str__(self):
        return f'Транспорт {self.color} цвета едет со скоростью {self.speed}'

    @abstractmethod
    def ride_earth(self):
        pass

    def ride_water(self):
        pass

    @property
    def color(self) -> str: # get
        return self._color

    @color.setter
    def color(self, new_color: str):
        self._color = new_color

    @property
    def speed(self) -> int: # get
        return self._speed

    @speed.setter
    def speed(self, new_speed: int):
        self._speed = new_speed


class Auto(Transport):

    def ride_earth(self):
        print('Я еду по земле')


class Boat(Transport):

    def ride_water(self):
        print('Я еду по воде')


class Amphibians(Auto, Boat, MusicMixin):
    pass


a = Amphibians(color='Red', speed=55)
a.music()
a.ride_earth()
a.ride_water()
print(a)
b = Auto(color='Blue', speed=105)
b.color = 'Yellow'
b.speed = 200
print(b.color)
print(b)
#############################################################
#PK 15.1

class File:
    """
    Класс "Контекст менеджер" File - Открывает файл и проверяет на наличие уже существующего.
        Attributes:
        filename - Наименование файла
        mode - Режим чтения/записи (r/w)
    """
    def __init__(self, filename: str, mode: str) -> None:
        print('Открывание файла')
        self.filename = filename
        self.mode = mode

    def __enter__(self) -> 'File':
        """
        Метод Enter - открывая в обработке файл с заданными атрибутами, если файл уже существует,
         то откроет в режим записи.
        :return: возвращает в глобальную переменную.
        """
        try:
            self.file = open(self.filename, self.mode, encoding='utf-8')
        except FileNotFoundError:
            self.file = open(self.filename, 'w', encoding='utf-8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Метод Exit - закрывает в завершение файл.
        :return: Возвращая True, подтверждая успешное завершение.
        """
        self.file.close()
        return True


with File('example.txt', 'r') as file:
    file.write('Всем привет!')
#############################################################
#PK 15.2
class MyMath:
    """
    Класс MyMath с различными математическими вычислениями.
    __pi: число пи
    """
    __pi = 3.1415926535

    @classmethod
    def circle_len(cls, radius: int) -> float:
        """
        Метод вычисления длины окружности (answer=2πR)
        :param radius: (int) радиус
        :return: (float) ответ
        """
        answer = 2 * cls.__pi * radius
        return answer

    @classmethod
    def area_circle(cls, radius: int) -> float:
        """
        Метод вычисления площади окружности (answer=πR²).
        :param radius: (int) радиус
        :return: (float) ответ
        """
        answer = cls.__pi * (radius ** 2)
        return answer

    @classmethod
    def cube_volume(cls, edge: int) -> int:
        """
        Метод вычисления объёма куба (answer=a³).
        :param edge: (int) радиус
        :return: (int) ответ
        """
        answer = edge ** 3
        return answer

    @classmethod
    def surface_area_sphere(cls, radius: int) -> float:
        """
        Метод площадь поверхности сферы (answer= 4πR²).
        :param radius: (int) радиус
        :return: (float) ответ
        """
        answer = (4 * cls.__pi) * (radius ** 2)
        return answer


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.area_circle(radius=6)
res_3 = MyMath.cube_volume(edge=3)
res_4 = MyMath.surface_area_sphere(radius=9)
print(res_1)
print(res_2)
print(res_3)
print(res_4)
############################################################
#PK 15.3
from typing import Any


class Date:
    """
    Класс Date, проверяет числа даты на корректность.
    Attributes:
        day(int) - день
        month(int) - месяц
        year(int) - год
    """
    day = 0
    month = 0
    year = 0

    @classmethod
    def from_string(cls, new_date: str) -> Any:
        """
        Метод преобразует из str в int присваивая атрибутам значения.
        :param new_date: входящая строка типового значения "14-08-2022" через дефис
        :return: полную информацию о дате.
        """
        cls.day = int(new_date[:2])
        cls.month = int(new_date[3:5])
        cls.year = int(new_date[6:])
        return f'День: {cls.day}    Месяц: {cls.month}    Год: {cls.year}'

    @classmethod
    def is_date_valid(cls, new_date: str) -> bool:
        """
        Метод проверяет на логические ошибки в дате.
        :param new_date: входящая строка типового значения "14-08-2022" через дефис
        :return: True или False.
        """
        flag = True
        Date.from_string(new_date)
        if cls.day > 31 or cls.month > 12:
            flag = False
        return flag


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
############################################################
#16.1
from collections.abc import Iterator
from contextlib import contextmanager
import time


@contextmanager
def timer() -> Iterator:
    start = time.time()
    try:
        yield
    except Exception as er:
        print(f'Ошибка: {er}')
    finally:
        print(f'Прошло времени: {time.time() - start}')


with timer() as answer:
    print('Первая часть')
    result = 100 * 100 ** 1000000
    result += "f"


with timer() as answer_2:
    print('Вторая часть')
    result_2 = 200 * 200 ** 1000000
############################################################
#16.2
from collections.abc import Iterator
from contextlib import contextmanager
import os


@contextmanager
def in_dir(address) -> Iterator:
    cur_path = os.getcwd()
    os.chdir(address)
    try:
        yield
    finally:
        os.chdir(cur_path)
# принимает в качестве аргумента путь и временно меняет текущую рабочую директорию на новую.

with in_dir('C:\Skillbox\Basic'):
    print(os.listdir())
############################################################
#16.2.1
from typing import Callable, Any


def repeat(number: int = 2) -> Callable:
    def do_twice(func: Callable) -> Callable:
        def wrapped_greeting(*args, **kwargs) -> Any:
            [func(*args, **kwargs) for _ in range(number)]
        return wrapped_greeting
    return do_twice


@repeat(number=6)
def greeting(name: str) -> Any:
    print('Привет, {name}!'.format(name=name))


greeting('Tom')
############################################################
#16.2.2
from typing import Callable, Any
import threading


def do_timer(_func=None, *, time_sec: int = 1) -> Callable:
    def timer(my_func: Callable) -> Any:
        def wrapped_func(*args, **kwargs):
            threading.Timer(time_sec, header).start()
            my_func(*args, **kwargs)
            return my_func
        return wrapped_func
    if _func is None:
        return timer
    return timer(_func)
# декоратор можно использовать как с аргументами, так и без них.


@do_timer(time_sec=5) # вот здесь можно писать и без аргументов
def header() -> Any:
    print('Title, html')


header()

############################################################
#29.1
import functools
from typing import Callable, Any


def check_permission(person: str) -> Any:
    """Декоратор для проверки прав пользователя.
    Возвращает ошибку или право доступа к функции"""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                if person == ''.join(user_permissions):
                    return func(*args, **kwargs)
                raise PermissionError
            except PermissionError:
                print('У пользователя недостаточно прав, чтобы выполнить функцию add_comment')
        return wrapper
    return decorator


user_permissions = ['admin']


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
############################################################
#29.2
import functools
from typing import Callable, Any


def callback(url: str) -> Any:
    """
    Функция, которая вызывается при срабатывании определённого события:
    переходе на страницу, получении сообщения или окончании обработки процессором.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f'Вызвана функция {func.__name__} по url-адресу {url}')
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


app = {'//': example}
route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
############################################################
#29.3
import time
from datetime import datetime
import functools


def timer(func, cls, date_time):
    """
    Функция timer обёртка от log_methods,
    которая преобразует дату и фиксирует затраченное время на выполнение методов класса.
    """
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        new_date = ['%' + letter if letter.isalpha() else letter for letter in date_time]
        new_date_symbol = ''.join(new_date)
        now = datetime.now()
        print(f'Запускается {cls.__name__}.{func.__name__}. Дата и время запуска: {now.strftime(new_date_symbol)}.')
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Завершение {cls.__name__}.{func.__name__}, время работы = {round(end - start, 3)} s. ')
        return result
    return wrapper


def log_methods(date_time: str):
    """
    Декоратор класса.
    Получает параметры даты и фиксирует время с помощью функции timer применяет его ко всем методам класса.
    """
    def decorate(cls):
        for i_method_name in dir(cls):
            if i_method_name.startswith('__') is False:
                cur_method = getattr(cls, i_method_name)
                decorated_method = timer(cur_method, cls, date_time)
                setattr(cls, i_method_name, decorated_method)
        return cls
    return decorate


@log_methods('b d Y - H:M:S')
class A:
    def test_sum_1(self) -> int:
        print('Тут метод test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods('b d Y - H:M:S')
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("Наследник test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
############################################################
#29.4
from typing import Callable, Any
import functools


def decorator_with_args_for_any_decorator(decorated_decorator: Callable) -> Callable: # оболочка Декоратора
    """
    Декорирует декоратор. Даёт возможность любому декоратору принимать произвольные аргументы.
    """
    @functools.wraps(decorated_decorator)  # Декорируемый декоратор
    def wrapped(*args, **kwargs): # Аргументы от @decorated_decorator(..,аргументы,..)
        def decorated_decorator(func): # Открывает функцию
            def wrapper(*decorated_decorator_args, **decorated_decorator_kwargs): # Cодержимое функции
                print(f'Переданные арги и кварги в декоратор: {args, kwargs}')
                result = func(*decorated_decorator_args, **decorated_decorator_kwargs) # запускает содержимое функции
                return result
            return wrapper
        return decorated_decorator
    return wrapped


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable) -> Any:
    """
    Декоратор функции. Вызывает(декорирует) содержимое функции
    """
    @functools.wraps(func)
    def wrapper(*func_args, **func_kwargs):
        result = func(*func_args, **func_kwargs)
        return result
    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)
############################################################
#29.4
import functools


def singleton(cls):
    """ Декоратор класса. Который превращает класс в одноэлементный"""
    @functools.wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance
    wrapper_singleton.instance = None
    return wrapper_singleton


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))
############################################################
#30.2 (ч. 1)
from typing import Callable, Any
import functools


def counter_2(func: Callable) -> Any:
    """
    Декоратор counter_2. Считает кол-во вызовов обёртки декоратора.
    Здесь применяем global
   """
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        global count
        count += 1
        temp = func(*args, **kwargs)
        print(f'Функция {func.__name__} вызвана: {count} раз')
        return temp
    return wrapped_func


@counter_2
def test() -> Any:
    print('test')


count = 0
test()
test()
############################################################
#30.2 (ч. 2)
from typing import Callable, Any
import functools
from collections.abc import Callable


def counter_2(func: Callable) -> Any:
    """
    Декоратор counter_2. Считает кол-во вызовов обёртки декоратора.
    Здесь применяем nonlocal
   """
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        nonlocal count
        count += 1
        temp = func(*args, **kwargs)
        print(f'Функция {func.__name__} вызвана: {count} раз')
        return temp
    count = 0
    return wrapped_func


@counter_2
def test() -> Any:
    print('test')


test()
test()
print(dir(__builtins__)) # Команда которая перечисляет все функции и методы,
# находящиеся во встроенном пространстве имён в Python
print(dir('.')) #Или это. Но они разные
############################################################
#30.2 (test)
def test():
    b = 5

    def test_2():
        a = 8
        if 'a' in globals():
            raise Exception
        if 'c' in locals():
            raise Exception
        print('b' in locals())
        print('b' in globals())
    test_2()

c = 4
test()
# b - in nonlocal
# c - in globals
# a - in locals
############################################################
#pk 30(1)
from typing import List
from functools import reduce


floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

if name == "__main__":
    result_float = list(map(lambda x: round(x**3, 3), floats))
    print(result_float)
    result_names = list(filter(lambda x: len(x) > 4, names))
    print(result_names)
    result_numbers = reduce(lambda x, y: x * y, numbers)
    print(result_numbers)
############################################################
#pk 30(2)
from typing import List

if name == "__main__":
    letters: List[str] = ['a', 'b', 'c', 'd', 'e']
    numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    result = list(map(lambda x, y: tuple(x + str(y)), letters, numbers))
    print(result)
############################################################
#pk 30(3)
from collections import deque

if __name__ == '__main__':
    def can_be_poly(word: str) -> bool:
        new_word = deque(word)
        new_word.reverse()
        if ''.join(new_word) == word:
            return True
        return False


    print(can_be_poly('abcba'))
    print(can_be_poly('abbbc'))

from abc import ABC, abstractmethod


class Figure(ABC):
    """
    Абстрактный класс Фигура
    """

    def __init__(self, pos_x: int, pos_y: int, length: int, width: int) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.length = length
        self.width = width

    @abstractmethod
    def move(self, pos_x: int, pos_y: int) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y


class ResizableMixin:
    def resize(self, length: int, width: int) -> None:
        self.length = length
        self.width = width


class Rectangle(Figure, ResizableMixin):
    """
    Прямоугольник
    """

    def move(self, pos_x: int, pos_y: int) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y


class Square(Figure, ResizableMixin):
    """ Квадрат """

    def __init__(self, pos_x: int, pos_y: int, size: int) -> None:
        super().__init__(pos_x, pos_y, size, size)

    def move(self, pos_x: int, pos_y: int) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y




rect_1 = Rectangle(pos_x=10, pos_y=20, length=5, width=6)
rect_2 = Rectangle(pos_x=30, pos_y=40, length=10, width=11)
square_1 = Square(pos_x=50, pos_y=70, size=7)


for figure in [rect_1, rect_2, square_1]:
    new_size_x = figure.length * 2
    new_size_y = figure.width * 2
    figure.resize(new_size_x, new_size_y)


test = Square(1, 2, 34)
print(Square.__name__)

#############################################################
from abc import ABC, abstractmethod


class MusicMixin:

    def music(self):
        print('Я свободен! Словно птица в небесах')


class Transport(ABC):

    @abstractmethod
    def ride_earth(self):
        pass

    @abstractmethod
    def ride_water(self):
        pass


class Auto(Transport):

    def ride_earth(self):
        print('Я еду по земле')


class Boat(Transport):

    def ride_water(self):
        print('Я еду по воде')


class Amphibians(Auto, Boat, MusicMixin):
    pass


a = Amphibians()
a.music()
a.ride_earth()
a.ride_water()

#############################################################
#Контекст менеджер

class File:
    def __init__(self, filename, mode) -> None:
        print('Открывание файла')
        self.filename = filename
        self.mode = mode
        self.start = None

    def __enter__(self) -> 'File':
        self.start = open(self.filename, self.mode, encoding='utf-8')
        return self.start

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.start.close()
        return True


with File('example.txt', 'w') as file:
    file.write('Всем привет!')

#############################################################
class Example:
    def __init__(self) -> None:
        print('Вызов __init__')

    def __enter__(self) -> 'Example':
        self.a = 'Вызов __enter__'
        print(self.a)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Вызов __exit__')
        if exc_type is Exception:
            return True


my_obj = Example()

with my_obj as obj:
    print('Код внутри первого вызова контекст менеджера')

    with my_obj as obj2:
        raise Exception('Выброс исключения во вложенном (втором) вызове контекст менеджере')

    print('Я обязательно выведусь...')
#############################################################
from abc import ABC, abstractmethod


class MusicMixin:

    def music(self):
        print('Я свободен! Словно птица в небесах')


class Transport(ABC):
    def __init__(self, color: str, speed: int) -> None:
        self._color = color
        self._speed = speed

    def __str__(self):
        return f'Транспорт {self.color} цвета едет со скоростью {self.speed}'

    @abstractmethod
    def ride_earth(self):
        pass

    def ride_water(self):
        pass

    @property
    def color(self) -> str: # get
        return self._color

    @color.setter
    def color(self, new_color: str):
        self._color = new_color

    @property
    def speed(self) -> int: # get
        return self._speed

    @speed.setter
    def speed(self, new_speed: int):
        self._speed = new_speed


class Auto(Transport):

    def ride_earth(self):
        print('Я еду по земле')


class Boat(Transport):

    def ride_water(self):
        print('Я еду по воде')


class Amphibians(Auto, Boat, MusicMixin):
    pass


a = Amphibians(color='Red', speed=55)
a.music()
a.ride_earth()
a.ride_water()
print(a)
b = Auto(color='Blue', speed=105)
b.color = 'Yellow'
b.speed = 200
print(b.color)
print(b)
#############################################################
#PK 15.1

class File:
    def __init__(self, filename: str, mode: str) -> None:
        print('Открывание файла')
        self.filename = filename
        self.mode = mode
        self.start = None

    def __enter__(self) -> 'File':
        try:
            self.file = open(self.filename, self.mode, encoding='utf-8')
        except FileNotFoundError:
            self.file = open(self.filename, 'w', encoding='utf-8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return True


with File('example.txt', 'r') as file:
    file.write('Всем привет!')
#############################################################
#PK 15.2
import math


class MyMath:
    __pi = math.pi
    """
    Класс MyMath
    """

    @classmethod
    def circle_len(cls, radius: int) -> float:
        answer = 2 * cls.__pi * radius
        return answer

    @classmethod
    def area_circle(cls, radius: int) -> float: #площадь окружности S=πR²
        answer = cls.__pi * (radius ** 2)
        return answer

    @classmethod
    def cube_volume(cls, edge: int) -> int: #объём куба V=a³
        answer = edge ** 3
        return answer

    @classmethod
    def surface_area_sphere(cls, radius: int) -> float: #площадь поверхности сферы  S = 4πR²
        answer = (4 * cls.__pi) * (radius ** 2)
        return answer


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.area_circle(radius=6)
res_3 = MyMath.cube_volume(edge=3)
res_4 = MyMath.surface_area_sphere(radius=9)
print(res_1)
print(res_2)
print(res_3)
print(res_4)
############################################################

class Date:
    day = 0
    month = 0
    year = 0

    @classmethod
    def from_string(cls, new_date: str):
        cls.day = int(new_date[:2])
        cls.month = int(new_date[3:5])
        cls.year = int(new_date[6:])
        return f'День: {cls.day}    Месяц: {cls.month}    Год: {cls.year}'

    @classmethod
    def is_date_valid(cls, new_date: str):
        flag = True
        Date.from_string(new_date)
        if cls.day > 31 or cls.month > 12:
            flag = False
        return flag


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
############################################################
import functools
from datetime import datetime
import time
from typing import Callable


def createtime(cls):
    """
    Декоратор класса. Выводит время создания  инстанса класса
    """
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        print('Время создания инстанса класса:', datetime.utcnow())
        instance = cls(*args, **kwargs)
        return instance
    return wrapper


def timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('Время работы функции: ', end - start)
        return result
    return wrapper


def for_all_decorated(decorator: Callable) -> Callable:
    """
    Декоратор класса.
    Получает другой декоратор и применяет  его ко всем методам класса.
    """
    @functools.wraps(decorator)
    def decorate(cls):
        for i_method_name in dir(cls):
            if i_method_name.startswith('__') is False:
                cur_method = getattr(cls, i_method_name)
                decorated_method = decorator(cur_method)
                setattr(cls, i_method_name, decorated_method)
        return cls
    return decorate


@createtime
@for_all_decorated(timer)
class MyMath:
    def __init__(self, max_number: int) -> None:
        self.max_number = max_number

    def square(self) -> int:
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(self.max_number)])

        return result

    def cube(self, number: int) -> int:
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 3 for i_num in range(self.max_number)])

        return result


my_func_1 = MyMath(max_number=1000)
my_func_1.square()
my_func_1.cube(number=300)
############################################################
#Домашка
import functools
import time
from datetime import datetime


def create_time(cls):
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        print('Время создания: ', datetime.now())
        instance = cls(*args, **kwargs)
        new_roster_method = [method for method in dir(cls) if method.startswith('__') is False]
        print('Методы:', ', '.join(new_roster_method))
        return instance
    return wrapper


@create_time
class MyMath:
    def __init__(self, max_number: int) -> None:
        self.max_number = max_number

    def square(self) -> int:
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(self.max_number)])

        return result

    def cube(self, number: int) -> int:
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 3 for i_num in range(self.max_number)])

        return result


my_func_1 = MyMath(max_number=1000)
time.sleep(2)
my_func_2 = MyMath(max_number=3000)
############################################################
#Домашка
import functools
from datetime import datetime
from collections.abc import Callable


def logging(cls):
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        file_log = open('ex.txt', 'a')
        file_log.write(f'Это {str(cls)} Дата создания: {str(datetime.utcnow())}\n')
        return file_log
    return wrapper


def for_all_loggins(decorator: Callable) -> Callable:
    """
    Декоратор класса.
    Получает другой декоратор и применяет  его ко всем методам класса.
    """
    @functools.wraps(decorator)
    def decorate(cls):
        for i_method_name in dir(cls):
            if i_method_name.startswith('__') is False:
                cur_method = getattr(cls, i_method_name)
                decorated_method = decorator(cur_method)
                setattr(cls, i_method_name, decorated_method)
        return cls
    return decorate
# def decorator(cls): #тоже декорирует всех. аналог
#     for i_method in dir(cls):
#         if i_method.startswith('__'):
#             continue
#         a = getattr(cls, i_method)
#         if hasattr(a, '__call__'):
#             decorated_a = logging(a)
#             setattr(cls, i_method, decorated_a)
#     return cls


@for_all_loggins(logging)
class MyHome:
    def __init__(self, price, name):
        self.price = price
        self.name = name

    def windows(self) -> None:
        pass

    def floors(self) -> None:
        pass

    def plot_area(self) -> None:
        pass


a = MyHome(price=100000, name='Дачный')
a.windows()
a.floors()
a.plot_area()
############################################################
#29.1
import functools
from typing import Callable, Any


def check_permission(person: str) -> Any:
    """Декоратор для проверки прав пользователя.
    Возвращает ошибку или право доступа к функции"""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                if person == ''.join(user_permissions):
                    return func(*args, **kwargs)
                raise PermissionError
            except PermissionError:
                print('У пользователя недостаточно прав, чтобы выполнить функцию add_comment')
        return wrapper
    return decorator


user_permissions = ['admin']


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
############################################################
#29.2
import functools
from typing import Callable, Any


def callback(url: str) -> Any:
    """
    Функция, которая вызывается при срабатывании определённого события:
    переходе на страницу, получении сообщения или окончании обработки процессором.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f'Вызвана функция {func.__name__} по url-адресу {url}')
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


app = {'//': example}
route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
############################################################
#29.3
import time
from datetime import datetime
import functools


def timer(func, cls, date_time):
    """
    Функция timer обёртка от log_methods,
    которая преобразует дату и фиксирует затраченное время на выполнение методов класса.
    """
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        new_date = ['%' + letter if letter.isalpha() else letter for letter in date_time]
        new_date_symbol = ''.join(new_date)
        now = datetime.now()
        print(f'Запускается {cls.__name__}.{func.__name__}. Дата и время запуска: {now.strftime(new_date_symbol)}.')
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Завершение {cls.__name__}.{func.__name__}, время работы = {round(end - start, 3)} s. ')
        return result
    return wrapper


def log_methods(date_time: str):
    """
    Декоратор класса.
    Получает параметры даты и фиксирует время с помощью функции timer применяет его ко всем методам класса.
    """
    def decorate(cls):
        for i_method_name in dir(cls):
            if i_method_name.startswith('__') is False:
                cur_method = getattr(cls, i_method_name)
                decorated_method = timer(cur_method, cls, date_time)
                setattr(cls, i_method_name, decorated_method)
        return cls
    return decorate


@log_methods('b d Y - H:M:S')
class A:
    def test_sum_1(self) -> int:
        print('Тут метод test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods('b d Y - H:M:S')
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("Наследник test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
############################################################
#29.4
from typing import Callable, Any
import functools


def decorator_with_args_for_any_decorator(decorated_decorator: Callable) -> Callable: # оболочка Декоратора
    """
    Декорирует декоратор. Даёт возможность любому декоратору принимать произвольные аргументы.
    """
    @functools.wraps(decorated_decorator)  # Декорируемый декоратор
    def wrapped(*args, **kwargs): # Аргументы от @decorated_decorator(..,аргументы,..)
        def decorated_decorator(func): # Открывает функцию
            def wrapper(*decorated_decorator_args, **decorated_decorator_kwargs): # Cодержимое функции
                print(f'Переданные арги и кварги в декоратор: {args, kwargs}')
                result = func(*decorated_decorator_args, **decorated_decorator_kwargs) # запускает содержимое функции
                return result
            return wrapper
        return decorated_decorator
    return wrapped


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable) -> Any:
    """
    Декоратор функции. Вызывает(декорирует) содержимое функции
    """
    @functools.wraps(func)
    def wrapper(*func_args, **func_kwargs):
        result = func(*func_args, **func_kwargs)
        return result
    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)
############################################################
#29.4
import functools


def singleton(cls):
    """ Декоратор класса. Который превращает класс в одноэлементный"""
    @functools.wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance
    wrapper_singleton.instance = None
    return wrapper_singleton


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

############################################################
#30.4(1)
grades = [
    {'name': 'Kenneth', 'score': 3}, {'name': 'Bebe', 'score': 41}, {'name': 'Joyce', 'score': 24},
    {'name': 'Richard', 'score': 37}, {'name': 'Marian', 'score': 44}, {'name': 'Jana', 'score': 45},
    {'name': 'Sarah', 'score': 90}, {'name': 'Eddie', 'score': 2}, {'name': 'Mary', 'score': 63},
    {'name': 'Ronald', 'score': 15}, {'name': 'David', 'score': 44}, {'name': 'Richard', 'score': 78},
    {'name': 'Warren', 'score': 7}, {'name': 'Alyssa', 'score': 13}, {'name': 'Lloyd', 'score': 52},
    {'name': 'Vanessa', 'score': 6}, {'name': 'Karen', 'score': 40}, {'name': 'James', 'score': 54},
    {'name': 'Annie', 'score': 87}, {'name': 'Glenn', 'score': 9}, {'name': 'Bruce', 'score': 68},
    {'name': 'Ramona', 'score': 64}, {'name': 'Jeannie', 'score': 22}, {'name': 'Aaron', 'score': 3},
    {'name': 'Ronnie', 'score': 47}, {'name': 'William', 'score': 94}, {'name': 'Sandra', 'score': 40},
                                        ]

# Решение через key
print(min(grades, key=lambda elem: elem['score']))
print(max(grades, key=lambda elem: elem['score']))
# Вывод исключительно очков:
print(min(grades, key=lambda elem: elem['score'])['score'])
print(max(grades, key=lambda elem: elem['score'])['score'])
############################################################
#30.4(2)
class Person:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __str__(self):
        return f'Меня зовут {self._name} и мне {self._age}\n'

    @property
    def age(self):
        return self._age

    @property
    def name(self):
        return self._name

    @age.setter
    def age(self, other_age):
        self._age = other_age

    @name.setter
    def name(self, word):
        self._name = word

    def __repr__(self):
        return f"({self._name}, {self._age})"


a = Person('Max', 23)
a.age = 88
b = Person('Nik', 44)
c = Person('Lola', 32)
roster = [a, b, c]
roster.sort(key=lambda elem: elem.age)
print(roster)
roster.sort(key=lambda elem: -elem.age)
print(roster)
############################################################
#30.5(1)
print(sorted(list(map(int, (number for number in input('Введите числа: ').split(' '))))))
#
num = input('Введите цифры: ')
print(sorted(list(map(lambda x: x, num.split()))))
#30.5(2)
text = input('Введите cтроку: ') #qWe456rtY
print(list(filter(lambda x: x.isalpha() and not x.istitle(), text)))
#30.5(3)
from functools import reduce

sentences = ["Nory was a Catholic", "because her mother was a Catholic", "and Nory’s mother was a Catholic",
             "because her father was a Catholic", "and her father was a Catholic",
             "because his mother was a Catholic", "or had been"]

w = ' '.join(sentences)
print(reduce(lambda x, y: w.count('was'), w))
############################################################
#pk 30.1
from typing import List
from functools import reduce


floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

if __name__ == "__main__":
    result_float = list(map(lambda x: round(x**3, 3), floats))
    print(result_float)

    result_names = list(filter(lambda x: len(x) > 4, names))
    print(result_names)

    result_numbers = reduce(lambda x, y: x * y, numbers)
    print(result_numbers)

############################################################
#pk 30.2
from typing import List


letters: List[str] = ['a', 'b', 'c', 'd', 'e']
numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]

result = list(map(lambda x, y: tuple(x + str(y)), letters, numbers))
print(result)
############################################################
#pk 30.3


############################################################
# 31dz
import re

text = 'How much wood would a woodchuck chuck if a woodchuck could chuck wood?'
result = re.match(r'wo', text)
print('Определить, начинается ли текст с шаблона wo (Поиск шаблона в начале строки):', result)
result_1 = re.search(r'wo', text)
print('Поиск первого найденного совпадения по шаблону:', result_1)
print('Содержимое найденной подстроки:', result_1.group(0))
print('Начальная позиция:', result_1.start())
print('Конечная позиция:', result_1.end())
result_2 = re.findall(r'wo', text)
print('Список всех упоминаний шаблона:', result_2)
result_3 = re.sub(r'wo', 'ЗАМЕНА', text)
print('Текст после замены:', result_3)
############################################################
# 31dz
import re

text = 'How much \wwood+?, would a \wwood+?chuck \dwwood+, chuck if a \wwood+?,chuck could chuck \wwood?,'
result_2 = re.findall(r'\\wwood\+\?', text) #Добавляем слэши чтобы результат стал таким: ['\\wwood+?,', '\\wwood+?,']
print('Список всех упоминаний шаблона:', result_2)
############################################################
# 31dz
import re
#Первый содержит все слова, которые начинаются на гласную букву латинского алфавита
# (в этот раз слово может состоять и из одной буквы, например I).
text = 'Even if they are djinns, I will get djinns that can outdjinn them.'
result = re.findall(r'\b[euioaEUIOA]\w*', text) # Выводит все слова на гласную букву(есть шпоргалка)
print(result)
############################################################
# 31dz

import re
# Второй содержит слова, которые начинаются на любой символ, кроме гласных букв латинского алфавита.
text = 'Even if they are djinns, I will get djinns that can outdjinn them.'
result = re.findall(r'\b[rtpsdfghjklzxcvbnm]\w+', text) # Выводит все слова на гласную букву(есть шпоргалка)
print(result)

############################################################
# 31dz
import re

text = 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009'
result = re.findall(r'\d{2}-\d{2}-\d{4}', text) # Выводит все слова на гласную букву(есть шпоргалка)
print(result) # ['12-05-2007', '11-11-2011', '12-01-2009']

############################################################
# 31dz
import requests
import json

my_test = requests.get('https://swapi.dev/api/people/4/')

data = json.loads(my_test.text) # десериализация JSON
data['name'] = 'BULL'
print(data)

with open('ser.json', 'w') as file:
    json.dump(data, file, indent=4) # сериализация JSON


with open('ser.json', 'r') as file:
    data = json.load(file) #Здесь load, а НЕ loasds, потому что работаем с файлом

print(data['films'])

############################################################
# 31dz
import swapi #$ pip install swapi

# print(swapi.get_film(1))
# Сейчас библиотека не работает, получить начало сюжета можно напрямую

result = requests.get("https://swapi.dev/api/films/1/")
json_dict = json.loads(result.text)
print(json_dict["opening_crawl"])

############################################################
# 31pk1
import re

text = """ Lorem ipsum dolor sit amet, consectetuer adipiscing elit. 
Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes,
nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. 
Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate 
"""

result = re.findall(r'\b\w{4}\b', text)
print(result)
############################################################
# 31pk2
import re

text = """ А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666"""

private_auto = re.findall(r'\b[АВЕКМНОРСТУХ]\d{3}\w+', text)
print(f'Список номеров частных автомобилей: {private_auto}')

taxi = re.findall(r'\b[АВЕКМНОРСТУХ]{2}\d+', text)
print(f'Список номеров такси: {taxi}')
############################################################
# 31pk3
# РЕШЕНИЕ В 2 способа, ТЗ несло мало ясности

import requests
import json

starships_attribute = ["name", "max_atmosphering_speed", "starship_class", "pilots"]# необходимые искомые атрибуты корабля
pilots_attribute = ["name", "height", "mass", "homeworld", "url"]# необходимые искомые атрибуты пилота

my_starships = requests.get('https://swapi.dev/api/starships/?search=Millennium')
# ищем корабль Millennium Falcon
roster = json.loads(my_starships.text) # десериализация JSON
my_starships = roster["results"]

data_starships = [{key: value} for attribute in my_starships for key, value in attribute.items()
                  if key in starships_attribute] # атрибуты корабля
pilot_attribute = [json.loads(requests.get(attribute).text) for attribute in data_starships[3]['pilots']]
# ccылки на пилотов проверяем на Respone 200 и загружаем в текст

data_pilot = [{key: value} for attribute in pilot_attribute for key, value in attribute.items()
              if key in pilots_attribute]# атрибуты пилотов

data_starships.extend(data_pilot)

with open('ser.json', 'w') as file:
    json.dump(data_starships, file, indent=4)
# сериализация

with open('ser.json', 'r') as file:
    data = json.load(file) # Здесь load, а НЕ loasds, потому что работаем с файлом

for param in data:
    print(param)

##########################################
#Второй способ

ship_name = "Millennium Falcon"  # название корабля, для которого получаем информацию
# делаем запрос на получение информации о корабле
ship_url = "https://swapi.dev/api/starships/?search=" + ship_name
ship_response = requests.get(ship_url)
ship_data = json.loads(ship_response.text)
# получаем ссылку на один корабль из ответа на запрос

ship_api_url = ship_data["results"][0]["url"]
ship_api_response = requests.get(ship_api_url)
ship_api_data = json.loads(ship_api_response.text)

# информация о корабле
ship_info = {
    "название": ship_api_data["name"],
    "максимальная скорость": ship_api_data["max_atmosphering_speed"],
    "класс": ship_api_data["starship_class"],
    "список пилотов": []
            }
# получаем информацию о пилотах из ссылок в ответе на запрос для корабля
for pilot_url in ship_api_data["pilots"]:
    pilot_api_response = requests.get(pilot_url)
    pilot_api_data = json.loads(pilot_api_response.text)
    # информация о каждом пилоте
    pilot_info = {
        "имя": pilot_api_data["name"],
        "рост": pilot_api_data["height"],
        "вес": pilot_api_data["mass"],
        "родная планета": pilot_api_data["homeworld"],
        "ссылка на информацию о родной планете": pilot_api_data["homeworld"]
    }
    ship_info["список пилотов"].append(pilot_info)
# вывод информации о корабле и пилотах в консоль
print(json.dumps(ship_info, indent=4, ensure_ascii=False))
# запись информации о корабле и пилотах в JSON-файл
with open("ship_info.json", "w", encoding="utf-8") as file:
    json.dump(ship_info, file, indent=4, ensure_ascii=False)
############################################################
# 31pk4
import re

roster = ['9999999999', '999999-999', '99999x9999']
word_number = ['первый', 'второй', 'третий', 'четвертый', 'пятый', 'шестой']

for index_word, number in enumerate(roster):
    if re.findall(r'[8-9]\d{9}', number):
        print(f'{word_number[index_word]} номер: всё в порядке')
    else:
        print(f'{word_number[index_word]} номер: не подходит')
############################################################
# 31pk5
import re

# В данном случае запрос request.get заменен на загрзку сайта из файла html
with open('examples.html', 'r') as file:
    text = file.read()
# По итогу вы так же получаете код сайта в виде одной строки

result = re.findall(r'<h3>(.*?)</h3>', text)
print(result)
############################################################
# 31pk6
import json


diff_list = ['services', 'staff', 'datetime']
with open('json_new.json', 'r') as file_json_new:
    roster_new = json.load(file_json_new)

with open('json_old.json', 'r') as file_json_old:
    roster_old = json.load(file_json_old)

result = {key: roster_new['data'][key] for key in diff_list if roster_new['data'][key] != roster_old['data'][key]}

print(result)
with open('result.json.', 'w') as file_result:
    json.dump(result, file_result, indent=4)
