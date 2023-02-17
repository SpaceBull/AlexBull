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

