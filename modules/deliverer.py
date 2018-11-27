class Deliverer:
    """Class representing a coffee deliverer."""

    def __init__(self, deliverer_json):
        """Initialize deliverer from json request."""
        self.name = deliverer_json['Name']
        self.number = self.format_number(deliverer_json['PhoneNumber'])

        # Shop will only be present on deliverer registration.
        if 'Shop' in deliverer_json:
            self.shop = deliverer_json['Shop']

    @staticmethod
    def format_number(number):
        """Format number as +1<number> to be compatible with Twilio."""
        if len(number) == 10:  # no +1
            number = '+1' + number
        elif len(number) == 11:  # begins with 1
            number = '+' + number
        return number
