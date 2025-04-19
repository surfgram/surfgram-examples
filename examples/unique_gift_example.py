from surfgram.types import UniqueGift
from typing import Callable


class ExampleUniqueGift(UniqueGift):
    """Example implementation of UniqueGift handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_unique_gift",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the UniqueGift event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.base_name (str): Human-readable name of the regular gift from which this unique gift was upgraded
        - update.name (str): Unique name of the gift. This name can be used in https://t.me/nft/... links and story areas
        - update.number (int): Unique number of the upgraded gift among gifts upgraded from the same regular gift
        - update.model (UniqueGiftModel): Model of the gift
        - update.symbol (UniqueGiftSymbol): Symbol of the gift
        - update.backdrop (UniqueGiftBackdrop): Backdrop of the gift
        """
        # Example implementation
        # Implement your handler logic here
        pass
