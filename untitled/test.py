import unittest

from lesson_17_Unit_Testing import Pizza,\
    Order, PIZZA_SMALL_SIZE, PAYMENT_BY_CARD, PAYMENT_BY_CASH, PIZZA_BIG_SIZE


class TestPizza(unittest.TestCase):

    def setUp(self):
        self.pizza_big = Pizza(PIZZA_BIG_SIZE)
        self.pizza_small = Pizza(PIZZA_SMALL_SIZE)

    def test_create_big_pizza(self):
        self.assertEqual(self.pizza_big.size, 1)

    def test_create_small_pizza(self):
        self.assertEqual(self.pizza_small.size, 0)

    def test_error_size_pizza(self):
        with self.assertRaises(TypeError):
            Pizza(3)

    def test_pizza_size_big(self):
        self.assertEqual(self.pizza_big.pizza_size, 'big size')

    def test_pizza_size_small(self):
        self.assertEqual(self.pizza_small.pizza_size, 'small size')


class TestOrder(unittest.TestCase):

    def setUp(self):
        self.order_cash = Order(PAYMENT_BY_CASH)
        self.order_card = Order(PAYMENT_BY_CARD)



if __name__ == "__main__":
    unittest.main()
