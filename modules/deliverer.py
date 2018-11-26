class Deliverer:
    """Class representing a coffee deliverer."""

    def __init__(self, deliverer_json):
        """Initialize deliverer from json request."""
        self.name = deliverer_json['Name']
        self.number = deliverer_json['PhoneNumber']
        self.shop = deliverer_json['Shop']
