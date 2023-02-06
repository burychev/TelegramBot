import telebot
from algorithms import func


bot = telebot.TeleBot('secret_token')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Приветик. Напиши слово/текст, которое хотел бы увидеть в русской раскладке')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Тебе уже ничего не поможет')


@bot.message_handler(content_types=["text"])
def smenaraskladki(message):
    result = func(message.text)
    bot.send_message(message.chat.id, result)


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print("error: " + str(e))
