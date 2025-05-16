from surfgram.types import ShippingOption
from typing import Callable


class ExampleShippingOption(ShippingOption):
    """Example implementation of ShippingOption handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_shipping_option",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the ShippingOption event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.id (str): Shipping option identifier
        - update.title (str): Option title
        - update.prices (List[LabeledPrice]): List of price portions
        """
        # Example implementation
        # Implement your handler logic here
        pass
