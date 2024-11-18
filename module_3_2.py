
def send_email(message, recipient, sender="university.help@gmail.com"): # сообщение и получатель, умолчанию - отправитель.
    #Проверка на корректность e-mail отправителя и получателя.
    if "@" not in recipient or not recipient.endswith(
            (".com", ".ru", ".net")) or "@" not in sender or not sender.endswith((".com", ".ru", ".net")): #проверяем окончание строк на содержание @.com/.ru/.net
        print('Невозможно отправить письмо!',  'с адреса: ', sender, "на адрес:", recipient)
    # Если же sender и recipient совпадают, то вывести "Нельзя отправить письмо самому себе!"
    elif sender == recipient and recipient == sender:
            print("Нельзя отправить письмо самому себе!")
    elif sender !="university.help@gmail.com":
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ!Письмо отправлено с адреса ", sender, "на адрес", recipient)
    else:

        print("Письмо успешно отправлено:", message, "с адреса:", sender, "для адресата:", recipient)
#тесты:
send_email('<<Это сообщение для проверки связи>>', 'vasyok1337@gmail.com')
send_email('<<Вы видите это сообщение как лучший студент курса!>>', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('<<Пожалуйста, исправьте задание>>', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('<<Напоминаю самому себе о вебинаре>>', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')