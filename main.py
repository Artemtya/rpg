import telebot
from config import TOKEN
from info import locations
from telebot import types
import json


bot = telebot.TeleBot(TOKEN)


#сохранение прогресса
def save_progress(user_id, location):
    cur_progress = {str(user_id): location}
    try:
        with open('progress.json', 'r') as file:
            progress = json.load(file)
            progress[str(user_id)] = location
        with open('progress.json', 'w') as file:
            json.dump(progress, file)
    except FileNotFoundError:
        with open('progress.json', 'w') as file:
            json.dump(cur_progress, file)

# Возобновление процесса
def load_progress(user_id):
    try:
        with open('progress.json', 'r') as file:
            progress = json.load(file)
        return progress.get(str(user_id))
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return None

@bot.message_handler(commands=['start'])
def handle_start(message):
    chat_id = message.chat.id
    save_progress(chat_id, 'location1')  # начальная  локация на 'location1'

    bot.send_message(chat_id, 'Добро пожаловать в текстовую RPG-игру! Начнем приключение.')


    send_location_info(chat_id)

# Обработка нажатия кнопок
@bot.message_handler(func=lambda message: True)
def handle_button_click(message):
    chat_id = message.chat.id
    selected_option = message.text
    current_location = locations.get(load_progress(chat_id), {})

    if current_location and 'options' in current_location:
        next_location = current_location['options'].get(selected_option)
        if next_location:
            save_progress(chat_id, next_location)
            send_location_info(chat_id)
        else:
            bot.send_message(chat_id, 'Выберите корректную опцию.')
    else:
        bot.send_message(chat_id, 'Произошла ошибка. Пожалуйста, начните игру заново.')


def send_location_info(chat_id):
    current_location = locations.get(load_progress(chat_id), {})
    if current_location:
        description = current_location.get('description', 'Описание отсутствует.')
        options = current_location.get('options', {})


        bot.send_message(chat_id, description)

        # Отправка фотографии
        photo_path = current_location.get('photo')
        if photo_path:
            with open(photo_path, 'rb') as photo:
                bot.send_photo(chat_id, photo)

        # Отправка кнопок
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for option_text in options:
            button = types.KeyboardButton(text=option_text)
            keyboard.add(button)

        bot.send_message(chat_id, 'Выберите действие:', reply_markup=keyboard)
    else:
        bot.send_message(chat_id, 'Произошла ошибка. Пожалуйста, начните игру заново.')

if __name__ == '__main__':
    bot.polling(none_stop=True)
