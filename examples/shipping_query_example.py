from surfgram.types import ShippingQuery
from typing import Callable


class ExampleShippingQuery(ShippingQuery):
    """Example implementation of ShippingQuery handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_shipping_query",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the ShippingQuery event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.id (str): Unique query identifier
        - update.from (User): User who sent the query
        - update.invoice_payload (str): Bot-specified invoice payload
        - update.shipping_address (ShippingAddress): User specified shipping address
        """
        # Example implementation
        # Implement your handler logic here
        pass
