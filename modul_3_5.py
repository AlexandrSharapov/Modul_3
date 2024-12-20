'''
Задача "Рекурсивное умножение цифр":
'''

def get_multiplied_digits(number): #целое число
    str_number = str(number) #строковое представление(str) числа number

    # можно выполнить только тогда, когда длина строкового представления str_number больше 1
    if len(str_number) > 1:
        first = int(str_number[0]) #первый символ из str_number в числовом представлении(int) на основании индекса
        return first * get_multiplied_digits(int(str_number[1:])) #умножаем первую цифру числа на результат работы этой же функции с числом, но уже без первой цифры.

     #Если str_number состоит из одной цифры, возвращается эта цифра
    else:
        #(уход от умножения на ноль) если наше число не = 0, возвращается 1 
        if int(str_number) != 0:
            return int(str_number)
        else:
            return 1

#Вывод на консоль:
result = get_multiplied_digits(40203)
print(result)

result2 = get_multiplied_digits(402030)
print(result2)
