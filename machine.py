from transitions import Machine


class Order():
    def __init__(self):
        self.pizza_size = None
        self.payment_method = None
        self.states = [
            'standby', 'starting', 'selected_size',
            'selected_payment_method', 'confirmed'
        ]
        self.transitions = [
            ['start', 'standby', 'starting'],
            ['size_select', 'starting', 'selected_size'],
            ['select_payment_method', 'selected_size', 'selected_payment_method'],
            ['confirm', 'selected_payment_method', 'confirmed'],
            ['not_confirm', 'selected_payment_method', 'standby'],
        ]
        self.machine = Machine(
            self, states=self.states, transitions=self.transitions,
            initial='standby'
        )

    def start_msg(self):
        return 'Какую пиццу вы хотите пиццу? Большую или маленькую?'

    def size_selected_msg(self):
        return 'Как вы будете платить?'

    def select_payment_method_msg(self):
        return (
            f'Вы хотите {self.pizza_size} пиццу, '
            f'оплата - {self.payment_method}?'
        )
    def confirmed_msg(self):
        return 'Спасибо за заказ'
    
    def not_confirmed_msg(self):
        return 'Заказ отменен'

    def except_msg(self):
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
