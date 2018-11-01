class Order:
    """Class representing a coffee order."""

    def __init__(self, order_json):
        """Initialize order from json request."""
        self.shop = order_json['shop']
        self.size = order_json['size']
        self.customer_name = order_json['name']
        self.drink_name = order_json['drink']
        self.customer_number = order_json['customer_number']
        self.location = order_json['location']
        self.details = order_json['details']

    def __str__(self):
        """Return string representation of an order."""
        return f'Order: {self.size} {self.drink_name} from {self.shop}\n' \
               f'Details: {self.details}\n' \
               f'Location: {self.location}\n' \
               f'Contact Info: {self.customer_name}, {self.customer_number}'
