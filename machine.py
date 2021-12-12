from transitions import Machine


class Order():
    def __init__(self):
        self.pizza_size = None
        self.payment_method = None
        self.states = [
            'standby', 'starting', 'selected_size',
            'selected_payment_method', 'end'
        ]
        self.transitions = [
            ['start', 'standby', 'starting'],
            ['size_select', 'starting', 'selected_size'],
            ['select_payment_method', 'selected_size', 'selected_payment_method'],
            ['confirm', 'selected_payment_method', 'end'],
            ['not_confirm', 'selected_payment_method', 'end'],
        ]
        self.machine = Machine(
            self, states=self.states, transitions=self.transitions,
            initial='standby'
        )

    def get_answer(self, text_msg):
        if text_msg == 'start':
            answer = 'Какую пиццу вы хотите пиццу? Большую или маленькую?'
            self.start()
        elif text_msg in ['маленькую', 'маленькая']:
            self.pizza_size = 'маленькую'
            answer = 'Как вы будете платить?'
            self.size_select()
        elif text_msg in ['большую', 'большая']:
            self.pizza_size = 'большую'
            answer = 'Как вы будете платить?'
            self.size_select()
        elif text_msg in ['наличкой', 'наличными', 'наликом']:
            self.payment_method = 'наличкой'
            answer = (
                f'Вы хотите {self.pizza_size} пиццу, '
                f'оплата - {self.payment_method}?'
            )
            self.select_payment_method()
        elif text_msg == 'да':
            answer = 'Спасибо за заказ'
            self.confirm()
        elif text_msg == 'нет':
            self.not_confirm()
            answer = 'Заказ отменен'
        else:
            answer = self.except_msg()
        return answer

    def except_msg(self):
        text = ''
        if self.is_standby():
            text = 'Нажмите /start'
        if self.is_starting():
            text = 'Можно заказать только маленькую или большую пиццы'
        if self.is_selected_size():
            text = 'Доступна оплата только наличными'
        if self.is_selected_payment_method():
            text = 'Подтвердить заказ - да\nОтменить заказ - нет'
        return text


if __name__ == '__main__':
    order = Order()
