from surfgram.types import OrderInfo
from typing import Callable


class ExampleOrderInfo(OrderInfo):
    """Example implementation of OrderInfo handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_order_info",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the OrderInfo event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.name (str): Optional. User name
        - update.phone_number (str): Optional. User's phone number
        - update.email (str): Optional. User email
        - update.shipping_address (ShippingAddress): Optional. User shipping address
        """
        # Example implementation
        # Implement your handler logic here
        pass
