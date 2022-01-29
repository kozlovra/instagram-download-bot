import telebot
from downloader import get_image


bot = telebot.TeleBot('<bot token>', parse_mode='Markdown')


@bot.message_handler(func=lambda message: True)
def echo_all(message):
  bot.send_chat_action(message.chat.id, 'typing')
  get_image(message.text)
  bot.send_chat_action(message.chat.id, 'upload_document')
  img = open('/instabot/img.jpg', 'rb')
  bot.send_document(message.chat.id, img)


if __name__ == '__main__':
  bot.infinity_polling()