'''
Задача "Однокоренные":
'''
def single_root_words(root_word, *other_words):

    same_words = [] # пустой список same_words
    root_word_lower = root_word.lower() # Перевод корневого слова в нижний регистр для сравнения без учета регистра согласно примечаниям b.

    # При помощи цикла for перебираем слова(word_) на предмет наличия одинакового корня
    for word_ in other_words:
        word_lower = word_.lower() #присваиваем нашему слову нижний регистр

        #находится ли текущее слово в корне слова или наоборот
        if word_lower in root_word_lower or root_word_lower in word_lower:
            same_words.append(word_)  #добавляем слова в same_words
    return same_words #конец цикла и возврат образованного списка same_words

#Поиск однокоренных
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')


print(result1)
print(result2)