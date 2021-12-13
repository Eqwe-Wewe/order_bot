from aiogram import Bot, Dispatcher, executor
from machine import Order
from config import TOKEN
import re


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
users = {}


@dp.message_handler(commands=['help'])
async def help_comm(message):
    await bot.send_message(
        message.from_user.id,
        (
            'Этот бот создан для решения тестового задания по обработке заказа'
            '\nНажмите /start для начала диалога'
        )
    )


@dp.message_handler()
async def send_message(message):
    text = await get_data(message)
    await bot.send_message(message.from_user.id, text)


async def get_data(message):
    chat = message.chat['id']
    if chat not in users:
        users[chat] = Order()
    order = users[chat]
    responce = order.get_answer(parsing(message.text))
    if order.is_end():
        del users[chat]
    return responce


def parsing(text):
    return ' '.join(re.findall(r'\s*(\w+)\s*', text)).lower()


if __name__ == '__main__':
    executor.start_polling(dp)
