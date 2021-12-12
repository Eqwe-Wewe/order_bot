from transitions import Machine


class Order():
    def __init__(self):
        self.pizza_size = None
        self.payment_method = None
        self.states = ['size_selected', 'select_payment_method', 'standby']
        self.transitions = [
            ['choose_size', 'standby', 'size_selected'],
            ['error_choose_size', 'standby', 'standby'],
            ['choose_payment', 'size_selected', 'select_payment_method'],
            ['error_choose_payment', 'size_selected', 'size_selected'],
            ['confirm', 'select_payment_method', 'standby'],
            ['error_confirm', 'select_payment_method', 'select_payment_method'],
            ['not_confirm', 'select_payment_method', 'size_selected'],
        ]
        self.machine = Machine(
            self, states=self.states, transitions=self.transitions,
            initial='standby'
        )

    def start(self):
        return 'Какую пиццу вы хотите заказать?'

    def size_selected(self):
        return 'Как вы будете платить?'

    def select_payment_method(self, size, method):
        return (
            f'вы хотите {self.pizza_size} пиццу, '
            f'оплата - {self.payment_method}?'
        )
    def confirmed(self):
        return 'Спасибо за заказ!'


if __name__ == '__main__':
    order = Order()
