from surfgram.types import UniqueGiftModel
from typing import Callable


class ExampleUniqueGiftModel(UniqueGiftModel):
    """Example implementation of UniqueGiftModel handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_unique_gift_model",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the UniqueGiftModel event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.name (str): Name of the model
        - update.sticker (Sticker): The sticker that represents the unique gift
        - update.rarity_per_mille (int): The number of unique gifts that receive this model for every 1000 gifts upgraded
        """
        # Example implementation
        # Implement your handler logic here
        pass
