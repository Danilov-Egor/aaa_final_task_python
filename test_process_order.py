from process_order import bake, delivery, pickup
import unittest
from unittest.mock import patch


class TestProcessOrder(unittest.TestCase):

    @patch('random.randint')
    def test_bake(self, mock_randint):
        mock_randint.return_value = 5
        self.assertEqual(bake('pepperoni'), 5)

    @patch('random.randint')
    def test_delivery(self, mock_randint):
        mock_randint.return_value = 2
        self.assertEqual(delivery('margherita'), 2)

    @patch('random.randint')
    def test_pickup(self, mock_randint):
        mock_randint.return_value = 3
        self.assertEqual(pickup('hawaiian'), 3)
