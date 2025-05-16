from surfgram.types import PaidMediaInfo
from typing import Callable


class ExamplePaidMediaInfo(PaidMediaInfo):
    """Example implementation of PaidMediaInfo handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_paid_media_info",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the PaidMediaInfo event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.star_count (int): The number of Telegram Stars that must be paid to buy access to the media
        - update.paid_media (List[PaidMedia]): Information about the paid media
        """
        # Example implementation
        # Implement your handler logic here
        pass
