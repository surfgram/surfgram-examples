from surfgram.types import PaidMessagePriceChanged
from typing import Callable


class ExamplePaidMessagePriceChanged(PaidMessagePriceChanged):
    """Example implementation of PaidMessagePriceChanged handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_paid_message_price_changed",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the PaidMessagePriceChanged event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.paid_message_star_count (int): The new number of Telegram Stars that must be paid by non-administrator users of the supergroup chat for each sent message
        """
        # Example implementation
        # Implement your handler logic here
        pass
