from surfgram.types import StarAmount
from typing import Callable


class ExampleStarAmount(StarAmount):
    """Example implementation of StarAmount handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_star_amount",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the StarAmount event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.amount (int): Integer amount of Telegram Stars, rounded to 0; can be negative
        - update.nanostar_amount (int): Optional. The number of 1/1000000000 shares of Telegram Stars; from -999999999 to 999999999; can be negative if and only if amount is non-positive
        """
        # Example implementation
        # Implement your handler logic here
        pass
