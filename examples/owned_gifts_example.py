from surfgram.types import OwnedGifts
from typing import Callable


class ExampleOwnedGifts(OwnedGifts):
    """Example implementation of OwnedGifts handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_owned_gifts",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the OwnedGifts event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.total_count (int): The total number of gifts owned by the user or the chat
        - update.gifts (List[OwnedGift]): The list of gifts
        - update.next_offset (str): Optional. Offset for the next request. If empty, then there are no more results
        """
        # Example implementation
        # Implement your handler logic here
        pass
