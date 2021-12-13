from transitions import Machine
from transitions.core import MachineError


class Order():
    def __init__(self):
        self.pizza_size = None
        self.payment_method = None
        self.states = [
            'standby', 'starting', 'size_selected',
            'payment_method_selected', 'end'
        ]
        self.transitions = [
            ['start', 'standby', 'starting'],
            ['choose_size', 'starting', 'size_selected'],
            ['choose_pay_method', 'size_selected', 'payment_method_selected'],
            ['confirm', 'payment_method_selected', 'end'],
            ['not_confirm', 'payment_method_selected', 'end'],
        ]
        self.machine = Machine(
            self, states=self.states, transitions=self.transitions,
            initial='standby'
        )

    def get_answer(self, text_msg):
        try:
            if text_msg == 'start':
                answer = 'Какую пиццу вы хотите пиццу? Большую или маленькую?'
                self.start()
            elif text_msg in ['маленькую', 'маленькая']:
                self.pizza_size = 'маленькую'
                answer = 'Как вы будете платить?'
                self.choose_size()
            elif text_msg in ['большую', 'большая']:
                self.pizza_size = 'большую'
                answer = 'Как вы будете платить?'
                self.choose_size()
            elif text_msg in ['наличкой', 'наличными', 'наликом']:
                self.payment_method = 'наличкой'
                answer = (
                    f'Вы хотите {self.pizza_size} пиццу, '
                    f'оплата - {self.payment_method}?'
                )
                self.choose_pay_method()
            elif text_msg == 'да':
                answer = 'Спасибо за заказ'
                self.confirm()
            elif text_msg == 'нет':
                self.not_confirm()
                answer = 'Заказ отменен'
            else:
                answer = self.except_msg()
        except MachineError:
            answer = self.except_msg()
        finally:
            return answer

    def except_msg(self):
        text = ''
        if self.is_standby():
            text = 'Нажмите /start'
        if self.is_starting():
            text = 'Можно заказать только маленькую или большую пиццы'
        if self.is_size_selected():
            text = 'Доступна оплата только наличными'
        if self.is_payment_method_selected():
            text = 'Подтвердить заказ - да\nОтменить заказ - нет'
        return text


if __name__ == '__main__':
    order = Order()
