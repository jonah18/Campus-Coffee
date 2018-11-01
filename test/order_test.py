from modules import Order
import unittest


class OrderTest(unittest.TestCase):
    """Tests for the Order class."""

    def setUp(self):
        self.order_json = {
            'shop': 'starbucks',
            'size': 'grande',
            'name': 'jonah',
            'drink': 'coffee',
            'customer_number': '123456789',
            'location': 'ugli',
            'details': 'cream and sugar'
        }

    def test_init(self):
        """Test Order creation."""
        order = Order(self.order_json)
        self.assertEqual(order.shop, 'starbucks')
        self.assertEqual(order.size, 'grande')
        self.assertEqual(order.customer_name, 'jonah')
        self.assertEqual(order.drink_name, 'coffee')
        self.assertEqual(order.customer_number, '123456789')
        self.assertEqual(order.location, 'ugli')
        self.assertEqual(order.details, 'cream and sugar')

    def test_str(self):
        """Test Order string representation."""
        expected = 'Order: grande coffee from starbucks\n' \
                   'Details: cream and sugar\n' \
                   'Location: ugli\n' \
                   'Contact Info: jonah, 123456789'
        order = Order(self.order_json)

        self.assertEqual(str(order), expected)


def order_suite():
    return unittest.TestLoader().loadTestsFromTestCase(OrderTest)
