def calculate_structure_sum(*args):
  total_sum = 0  #приводим общую сумму как 0

  def recursive_sum(element):
    nonlocal total_sum
    # Все числа (не важно, являются они ключами или значениям или ещё чем-то)
    if isinstance(element, (int, float)):
      total_sum += element
    # Все строки (не важно, являются они ключами или значениям или ещё чем-то)
    elif isinstance(element, str):
      total_sum += len(element)
    elif isinstance(element, (list, tuple, set)):  #является ли коллекцией
      for item in element:
        recursive_sum(item)  # вызов функции на каждый элемент
    elif isinstance(element, dict):  # является ли словарем
      for key, value in element.items():
        recursive_sum(key)  # вызов функции на каждый ключ
        recursive_sum(value)  # вызов функции на значения

  # рекурсивное суммирование для каждого аргумента
  for element in args:
    recursive_sum(element)

  return total_sum  #возвращаем общую сумму

#Входные данные (применение функции)
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)

# Вывод результата
print(result)