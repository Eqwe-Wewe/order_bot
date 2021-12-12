from aiogram import Bot, Dispatcher, executor
from machine import Order
from config import TOKEN
import re


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
users = {}


@dp.message_handler(commands=['help'])
async def help_comm(message):
    await message.reply(
        'Этот бот создан для решения тестового задания по обработке заказа\n'
        'Нажмите /start для начала диалога'
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
    text_msg = parsing(message.text)
    if text_msg == 'start':
        text = order.start_msg()
        order.start()
    elif text_msg in ['маленькую', 'маленькая']:
        order.pizza_size = 'маленькую'
        text = order.size_selected_msg()
        order.size_select()
    elif text_msg in ['большую', 'большая']:
        order.pizza_size = 'большую'
        text = order.size_selected_msg()
        order.size_select()
    elif text_msg in ['наличкой', 'наличными', 'наликом']:
        order.payment_method = 'наличкой'
        text = order.select_payment_method_msg()
        order.select_payment_method()
    elif text == 'да':
        text = order.confirmed_msg()
        order.confirm()
        del users[chat]
    elif text == 'нет':
        order.not_confirm()
        text = order.not_confirmed_msg()
    else:
        text = order.except_msg()
    return text


def parsing(text):
    return ' '.join(re.findall('\s*(\w+)\s*',text)).lower()


if __name__ == '__main__':
    executor.start_polling(dp)
