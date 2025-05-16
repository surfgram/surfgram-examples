from surfgram.types import ShippingAddress
from typing import Callable


class ExampleShippingAddress(ShippingAddress):
    """Example implementation of ShippingAddress handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_shipping_address",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the ShippingAddress event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.country_code (str): Two-letter ISO 3166-1 alpha-2 country code
        - update.state (str): State, if applicable
        - update.city (str): City
        - update.street_line1 (str): First line for the address
        - update.street_line2 (str): Second line for the address
        - update.post_code (str): Address post code
        """
        # Example implementation
        # Implement your handler logic here
        pass
