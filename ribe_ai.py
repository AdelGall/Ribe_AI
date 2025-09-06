import os
import telebot
import whisper

from dotenv import load_dotenv

file_name = '.env'

load_dotenv()

model = whisper.load_model("base")
token_bot = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(token_bot, parse_mode=None)

dir = os.path.dirname(__file__)

@bot.message_handler(content_types=['text'])
def send_welcome(message):
    bot.reply_to(message, "Здравствуй, отправь аудио-файл для транскрибации")

@bot.message_handler(content_types=['audio'])
def echo_all(message):
    file = bot.get_file(message.audio.file_id)
    downloaded_file = bot.download_file(file.file_path)
    audio_name = message.audio.file_name
    with open(audio_name, 'wb') as f:
        f.write(downloaded_file)
    bot.reply_to(message, "Файл получен, начинается транскрибация, это может занять какое-то время...")
    result = transcribe_audio(f'{dir}/{audio_name}')
    send_long_message(message.chat.id, result)
    bot.reply_to(message, "Конец транскрибации")
    os.remove(f'{dir}/{audio_name}')

def send_long_message(chat_id, text):
    max_len = 4096
    for i in range(0, len(text), max_len):
        chunk = text[i:i+max_len]
        if len(chunk) > max_len:
            chunk = chunk[:max_len]
        bot.send_message(chat_id, chunk)


def transcribe_audio(file_path):
    result = model.transcribe(file_path)
    return result["text"]

bot.polling(none_stop=True)