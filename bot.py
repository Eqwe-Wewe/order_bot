import requests
import re
from config import TOKEN
from transitions import Machine


URL = r'https://api.telegram.org/bot' + TOKEN


class Order(object):

    states = [
        'size_selected', 'select_payment_method', 'standby'
    ]

    transitions = [
        {'trigger': 'choose_size', 'source': 'standby', 'dest': 'size_selected'},
        {'trigger': 'choose_payment', 'source': 'size_selected', 'dest': 'select_payment_method'},
        {'trigger': 'confirm', 'source': 'select_payment_method', 'dest': 'standby'},
    ]

    def __init__(self):
        self.machine = Machine(
            self, states=Order.states, transitions=Order.transitions,
            initial='standby'
        )


class Var():

    def __init__(self):
        self.pizza_size = None
        self.payment_method = None


users_property = {}

 
def get_update():
    return requests.get(f'{URL}/getUpdates').json()


def get_data():
    updates = get_update()
    chat_id = updates['result'][-1]['message']['chat']['id']
    text = updates['result'][-1]['message']['text']
    last_update_id = updates['result'][-1]['update_id']
    return {
        'chat_id': chat_id,
        'text': text,
        'last_update_id': last_update_id
    }


def get_message():
    message = get_data()
    chat = message['chat_id']
    text = parsing(message['text'])

    if text is not None:
        if chat not in users_property:
            users_property[chat] = Var()
            users_property[chat].machine = Order()
        if text.lower() == 'start':
            answer(chat, 'Какую пиццу вы хотите заказать?')
        elif text.lower() in ['большую', 'большая']:
            users_property[chat].pizza_size = 'большую'
            text = 'как вы будете платить?'
            answer(chat, text)
        elif text.lower() == 'наличкой':
            users_property[chat].payment_method = 'наличкой'
            text = (
                f'вы хотите {users_property[chat].pizza_size} пиццу, '
                f'оплата - {users_property[chat].payment_method}?'
            )
            answer(chat, text)
        elif text.lower() == 'да':
            text = 'Спасибо за заказ!'
            answer(chat, text)


def answer(chat_id, text):
    requests.get(f'{URL}/sendmessage?chat_id={chat_id}&text={text}')


def parsing(text):
    return ' '.join(re.findall('\s*(\w+)\s*',text))


def main():
    #get_message()
    update_id = get_data()['last_update_id']
    while True:
        current_id = get_data()['last_update_id']
        if update_id != current_id:
            get_message()
            update_id = get_data()['last_update_id']


if __name__ == '__main__':
    main()
