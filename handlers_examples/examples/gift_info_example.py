from surfgram.types import GiftInfo
from typing import Callable


class ExampleGiftInfo(GiftInfo):
    """Example implementation of GiftInfo handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_gift_info",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the GiftInfo event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.gift (Gift): Information about the gift
        - update.owned_gift_id (str): Optional. Unique identifier of the received gift for the bot; only present for gifts received on behalf of business accounts
        - update.convert_star_count (int): Optional. Number of Telegram Stars that can be claimed by the receiver by converting the gift; omitted if conversion to Telegram Stars is impossible
        - update.prepaid_upgrade_star_count (int): Optional. Number of Telegram Stars that were prepaid by the sender for the ability to upgrade the gift
        - update.can_be_upgraded (bool): Optional. True, if the gift can be upgraded to a unique gift
        - update.text (str): Optional. Text of the message that was added to the gift
        - update.entities (List[MessageEntity]): Optional. Special entities that appear in the text
        - update.is_private (bool): Optional. True, if the sender and gift text are shown only to the gift receiver; otherwise, everyone will be able to see them
        """
        # Example implementation
        # Implement your handler logic here
        pass
