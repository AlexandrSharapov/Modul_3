
calls = 0 #вне функций
#count_calls изменяет значение переменной calls. Эта функция должна вызываться в остальных двух функциях.
def count_calls():
    global calls
    calls += 1

#принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
def string_info(string):
    count_calls() #Исполнение пункта 1. Вызов функции глобальной
    return (len(string), string.upper(), string.lower())

#принимает два аргумента: строку и список, возвращает True - если строка находится в этом списке, False - если отсутствует
def is_contains(string, list_to_search):
    count_calls() #Исполнение пункта 1. Вызов функции глобальной
    is_contained = False # is_contained назначаем значение False
    for substring in list_to_search: # перебираем списки с помощью цикла for
        if substring in string:
            is_contained = True
    return is_contained

#Вывод на консоль:
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
#Вывести значение переменной calls на экран(в консоль).
print(calls)