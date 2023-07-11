from telegram.ext import Updater, MessageHandler, Filters

# Обработчик сообщений с эмодзи
def handle_emoji(update, context):
    message = update.message
    emojis = message.parse_entities(types='emoji')
    
    if emojis:
        # Получаем список расшифрованных эмодзи
        emoji_names = [emoji.description for emoji in emojis]
        
        # Отправляем расшифрованные эмодзи обратно пользователю
        reply_text = "Расшифрованные эмодзи: {}".format(", ".join(emoji_names))
        message.reply_text(reply_text)
    else:
        # Если сообщение не содержит эмодзи
        message.reply_text("Сообщение не содержит эмодзи.")

def main():
    # Замените 'TOKEN' на ваш токен бота
    updater = Updater('6346274956:AAHt8g9dNwtkiyDFH3fBuVxF2vl2__kNIQk', use_context=True)
    dp = updater.dispatcher
    
    # Создаем обработчик сообщений с эмодзи
    emoji_handler = MessageHandler(Filters.text, handle_emoji)
    dp.add_handler(emoji_handler)
    
    # Запускаем бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()