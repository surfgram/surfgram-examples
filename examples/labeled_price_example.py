from surfgram.types import LabeledPrice
from typing import Callable


class ExampleLabeledPrice(LabeledPrice):
    """Example implementation of LabeledPrice handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_labeled_price",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the LabeledPrice event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.label (str): Portion label
        - update.amount (int): Price of the product in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
        """
        # Example implementation
        # Implement your handler logic here
        pass
