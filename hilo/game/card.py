import random

class Card:
    """part of a set of rectangular pieces of cardboard or other material 
    with an identical pattern on one side and different numbers and symbols on the other.

    The responsibility of the Card is to keep track of the displayed number.

    Attributes:
        current_card (int): A random card between 1-13.
        next_card (int): A second random card between 1-13.
    """

    def __init__(self):
        """Constructs a new instance of Card with a value of the current, the next card and points.

        Args:
            self (Card): An instance of Card.
        """
        self.current_card = 0
        self.next_card = 0


    def random_card(self):
        """Generates a new random value.
        
        Args:
            self (Card): An instance of Card.
        """
        self.current_card = random.randint(1, 13)
        self.next_card = random.randint(1, 13)

        