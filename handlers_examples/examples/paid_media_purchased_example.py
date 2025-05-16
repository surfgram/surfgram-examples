from surfgram.types import PaidMediaPurchased
from typing import Callable


class ExamplePaidMediaPurchased(PaidMediaPurchased):
    """Example implementation of PaidMediaPurchased handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_paid_media_purchased",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the PaidMediaPurchased event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.from (User): User who purchased the media
        - update.paid_media_payload (str): Bot-specified paid media payload
        """
        # Example implementation
        # Implement your handler logic here
        pass
