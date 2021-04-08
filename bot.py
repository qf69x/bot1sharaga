import telebot
import configure

client = telebot.TeleBot(configure.config['token'])


@client.message_handler(content_types = ['text'])
def get_text(message):
    if message.text.lower() == '/all':
        client.send_message(message.chat.id, '@wepixi, @NEIZBESTNI, @nitekks, @Zandar25, @YARIKBOMBER22defbafff, @NaMax1malcah')


client.polling(none_stop = True, interval = 0)