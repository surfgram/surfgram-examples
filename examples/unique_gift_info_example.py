from surfgram.types import UniqueGiftInfo
from typing import Callable


class ExampleUniqueGiftInfo(UniqueGiftInfo):
    """Example implementation of UniqueGiftInfo handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_unique_gift_info",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the UniqueGiftInfo event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.gift (UniqueGift): Information about the gift
        - update.origin (str): Origin of the gift. Currently, either "upgrade" or "transfer"
        - update.owned_gift_id (str): Optional. Unique identifier of the received gift for the bot; only present for gifts received on behalf of business accounts
        - update.transfer_star_count (int): Optional. Number of Telegram Stars that must be paid to transfer the gift; omitted if the bot cannot transfer the gift
        """
        # Example implementation
        # Implement your handler logic here
        pass
