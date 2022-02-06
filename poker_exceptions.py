class IncorrectNumberOfCardsError(Exception):
    """Raised when the hand does not have 5 cards"""

    def __init__(self, card_number: int):
        self.message = f"Hand has incorrect number of cards. Current hand has {card_number} cards. To play hand should have 5 cards."
        super().__init__(self.message)
