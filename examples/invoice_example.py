from surfgram.types import Invoice
from typing import Callable


class ExampleInvoice(Invoice):
    """Example implementation of Invoice handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_invoice",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the Invoice event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.title (str): Product name
        - update.description (str): Product description
        - update.start_parameter (str): Unique bot deep-linking parameter that can be used to generate this invoice
        - update.currency (str): Three-letter ISO 4217 currency code, or "XTR" for payments in Telegram Stars
        - update.total_amount (int): Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
        """
        # Example implementation
        # Implement your handler logic here
        pass
