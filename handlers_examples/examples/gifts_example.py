from surfgram.types import Gifts
from typing import Callable


class ExampleGifts(Gifts):
    """Example implementation of Gifts handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_gifts",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the Gifts event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.gifts (List[Gift]): The list of gifts
        """
        # Example implementation
        # Implement your handler logic here
        pass
