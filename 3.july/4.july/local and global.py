IMPORTANT_ID = 12233125




def send_message(message):
    print(f'Сообщение было отправлено пользователю {IMPORTANT_ID}: ' + message)

send_message('тест')

print(send_message.__globals__)
