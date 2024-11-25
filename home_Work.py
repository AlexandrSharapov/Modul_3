import tkinter as tk #Библиотека тикейинтер и сокращаем ее имя на tk
from tkinter.ttk import Button

def get_valles():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2

def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)




def add():#summ
    num1, num2 = get_valles()
    res = num1 + num2
    insert_values(res)


def sub():#минус
    num1, num2 = get_valles()
    res = num1 - num2
    insert_values(res)


def div():#деление
    num1, num2 = get_valles()
    res = num1 / num2
    insert_values(res)

def mul():#умножение
    num1, num2 = get_valles()
    res = num1 * num2
    insert_values(res)

window = tk.Tk() #Создаем интерфейс, наше окошко

window.title('Калькулятор') #Имя окна
window.geometry("350x350") #Размер окна
window.resizable(False, False) #Зaпрещаем изменение окна нашей программы
#Виджеты
button_add = tk.Button(window, text = "+", width = 2, height=2, command=add) #Размещение какого либо виджета на форме (кнопка), ее название, размер.
button_add.place(x=100, y=200) #добавление объекта с координатами где он будет находиться

button_add = tk.Button(window, text = "-", width = 2, height=2, command=sub)
button_add.place(x=150, y=200)

button_add = tk.Button(window, text = "*", width = 2, height=2, command=mul)
button_add.place(x=200, y=200)

button_add = tk.Button(window, text = "/", width = 2, height=2, command=div)
button_add.place(x=250, y=200)

number1_entry = tk.Entry(window, width=28) #добавление текстового поля из библиотеки
number1_entry.place(x=100, y=75)
number1 = tk.Label(window, text="Введите первое число") #надписи
number1.place(x=100, y=50)

number2_entry = tk.Entry(window, width=28)
number2_entry.place(x=100, y=120)
number2 = tk.Label(window, text="Введите второе число")
number2.place(x=100, y=95)

answer_entry = tk.Entry(window, width=28)
answer_entry.place(x=100, y=300)
answer = tk.Label(window, text="Результат")
answer.place(x=100, y=275)

window.mainloop() #Обновление информации/событий и отвечает
