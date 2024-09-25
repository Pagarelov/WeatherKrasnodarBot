from telebot import telebot
import requests
import json

bot = telebot.TeleBot('Your Token')
API = 'Your API'

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, f'Hi!')
    city = 350000
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city},RU&appid={API}&units=metric')
    data = json.loads(res.text)
    temp_min = data["main"]["temp_min"]
    temp_max = data["main"]["temp_max"]
    weather_description = data["weather"][0]["description"]
    bot.send_message(message.chat.id, f'Weather in Krasnodar right now: min - {temp_min}°C, max - {temp_max}°C. Weather is: {weather_description}')

bot.polling(non_stop=True)
