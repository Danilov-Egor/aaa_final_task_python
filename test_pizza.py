from pizza import *
import unittest


class TestPizza(unittest.TestCase):

    def test_pizza_eq(self):
        pizza1 = Margherita('L')
        pizza2 = Margherita('L')
        self.assertEqual(pizza1, pizza2)

    def test_pizza_neq(self):
        pizza1 = Margherita('L')
        pizza2 = Margherita('XL')
        self.assertNotEqual(pizza1, pizza2)

    def test_pizza_diff_pizzas(self):
        pizza1 = Pepperoni('L')
        pizza2 = Margherita('XL')
        self.assertNotEqual(pizza1, pizza2)
