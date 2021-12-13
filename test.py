import unittest
from machine import Order
from bot import parsing


class TestOrder(unittest.TestCase):
    def setUp(self):
        self.order = Order()

    def test_answer_to_the_start_msg(self):
        self.assertEqual(
            self.order.get_answer(parsing('/start')),
            'Какую пиццу вы хотите пиццу? Большую или маленькую?'
        )

    def test_answer_to_the_pizza_size_msg(self):
        self.order.get_answer(parsing('/start'))
        self.assertEqual(
            self.order.get_answer(parsing('Большую')),
            'Как вы будете платить?'
        )

    def test_answer_to_the_payment_meth_msg(self):
        self.order.get_answer(parsing('/start'))
        self.order.get_answer(parsing('Большую'))
        self.assertEqual(
            self.order.get_answer(parsing('Наличкой')),
            (
                'Вы хотите большую пиццу, '
                'оплата - наличкой?'
            )
        )

    def test_answer_to_the_confirm_msg(self):
        self.order.get_answer(parsing('/start'))
        self.order.get_answer(parsing('Большую'))
        self.order.get_answer(parsing('Наличкой'))
        self.assertEqual(
            self.order.get_answer(parsing('Да')),
            ('Спасибо за заказ')
        )

    def test_dialog(self):
        self.order.get_answer(parsing('/start'))
        self.order.get_answer(parsing('Большую'))
        self.order.get_answer(parsing('Наличкой'))
        self.order.get_answer(parsing('Да'))
        self.assertTrue(self.order.is_end())


if __name__ == "__main__":
    unittest.main()
