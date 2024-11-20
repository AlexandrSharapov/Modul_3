'''
Задача "Распаковка"
'''

def print_params(a = 1, b = 'строка', c = True): #принимает три параметра со значениями по умолчанию
    print(a, b, c)

#Вызов print_params с разным количеством аргументов, включая вызов без аргументов.
print_params()
print_params(b = 25)
print_params(c = [1,2,3])


values_list = [11, 'Это_Список', (1,2,3)] #список с тремя элементами разных типов.
values_dict = {'a': 21, 'b': 'Это_словарь', 'c': True} #словарь c тремя ключами  = print_params и значениями разных типов
#распаковку параметров (* для списка и ** для словаря) values_list и values_dict в функцию print_params
print_params(*values_list)
print_params(**values_dict)

#Распаковка + отдельные параметры:
values_list_2 = [54.32, 'Строка' ]#список с двумя элементами разных типов
values_dict_3 = {'a': 11, 'b': 'kwargs', 'c': 30}
print_params(*values_list_2, 42)
print_params(**values_dict_3)