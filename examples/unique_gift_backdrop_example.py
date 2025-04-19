from surfgram.types import UniqueGiftBackdrop
from typing import Callable


class ExampleUniqueGiftBackdrop(UniqueGiftBackdrop):
    """Example implementation of UniqueGiftBackdrop handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_unique_gift_backdrop",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the UniqueGiftBackdrop event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.name (str): Name of the backdrop
        - update.colors (Union[UniqueGiftBackdropCol, s]): Colors of the backdrop
        - update.rarity_per_mille (int): The number of unique gifts that receive this backdrop for every 1000 gifts upgraded
        """
        # Example implementation
        # Implement your handler logic here
        pass
