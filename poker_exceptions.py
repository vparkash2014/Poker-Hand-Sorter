class IncorrectNumberOfCardsError(Exception):
    """Raised when the hand does not have 5 cards"""

    def __init__(self, card_number: int):
        self.message = f"The Showdown has incorrect number of cards. The current showdown has {card_number} cards. To play, the number of cards should be divisble by five."
        super().__init__(self.message)
