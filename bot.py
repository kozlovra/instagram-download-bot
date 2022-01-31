import telebot, os
from app import parse
from config import cfg_bot_token


bot = telebot.TeleBot(cfg_bot_token, parse_mode='Markdown')


@bot.message_handler(func=lambda message: True)
def echo_all(message):
  bot.send_chat_action(message.chat.id, 'upload_photo')
  parse(message.text)
  img = open(f"{os.path.dirname(os.path.abspath(__file__))}/photo.jpg", 'rb')
  bot.send_document(message.chat.id, img)


if __name__ == '__main__':
  bot.infinity_polling()