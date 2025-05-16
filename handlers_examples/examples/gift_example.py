from surfgram.types import Gift
from typing import Callable


class ExampleGift(Gift):
    """Example implementation of Gift handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_gift",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the Gift event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.id (str): Unique identifier of the gift
        - update.sticker (Sticker): The sticker that represents the gift
        - update.star_count (int): The number of Telegram Stars that must be paid to send the sticker
        - update.upgrade_star_count (int): Optional. The number of Telegram Stars that must be paid to upgrade the gift to a unique one
        - update.total_count (int): Optional. The total number of the gifts of this type that can be sent; for limited gifts only
        - update.remaining_count (int): Optional. The number of remaining gifts of this type that can be sent; for limited gifts only
        """
        # Example implementation
        # Implement your handler logic here
        pass
