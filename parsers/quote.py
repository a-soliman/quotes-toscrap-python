from locators.quote_locators import QuoteLocators


class QuoteParser:
    """
    given one quote div, find out the data (quote content)
    """

    def __init___(self, parent):
        self.parent = parent
