from decimal import Decimal

TWOPLACES = Decimal(10) ** -2


class DenominationConstants:
    """
    Choices used in origin field model of Products class.
    """
    OFICIAL = 'oficial'
    BLUE = 'blue'
    OFICIAL_EURO = 'oficial_euro'
    BLUE_EURO = 'blue_euro'

    CHOICES = (
        (OFICIAL, ("USD Oficial")),
        (BLUE, ("USD Blue")),
        (OFICIAL_EURO, ("Euro Oficial")),
        (BLUE_EURO, ("Euro Blue"))
    )
