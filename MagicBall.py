import random

print('╔=================================================================╗')
print('║                            MAGIC BALL                           ║')
print('║                                                                 ║')
print('║     Cпроси у Магического Шара любой вопрос, и жми любую кнопку. ║')
print('║                                                                 ║')
print('╚=================================================================╝')

count = 15
magic_answer = ['Разумеется', 'Всё как ты любишь)',
                'Определенно да', 'Спроси по увереннее',
                'Нет', 'Странный вопрос конечно, давай что нибудь другое',
                'В твоей последней песне был ответ', 'Если - бы',
                'Есть сомнения', ]
while True:
    result = input('\nГотовы.. ?)')
    loading = random.randint(70, 99)
    print(f'Загрузка... █████████████▒ {loading}%')
    print(f'MAGIC BALL: {random.choice(magic_answer)}')
    count -= 1
    if count == 10:
        print('ИИ: Ты так много хочешь знать, потом плохо будешь спать...')
    elif count == 5:
        print('ИИ: уже установил связь с твоими предками, они дали новые ответы')
    elif count == 0:
        print('ИИ: За следующий вопрос, ИИ потребует твою душу')