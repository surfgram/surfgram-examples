from surfgram.types import OwnedGiftRegular
from typing import Callable


class ExampleOwnedGiftRegular(OwnedGiftRegular):
    """Example implementation of OwnedGiftRegular handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_owned_gift_regular",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the OwnedGiftRegular event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the gift, always "regular"
        - update.gift (Gift): Information about the regular gift
        - update.owned_gift_id (str): Optional. Unique identifier of the gift for the bot; for gifts received on behalf of business accounts only
        - update.sender_user (User): Optional. Sender of the gift if it is a known user
        - update.send_date (int): Date the gift was sent in Unix time
        - update.text (str): Optional. Text of the message that was added to the gift
        - update.entities (List[MessageEntity]): Optional. Special entities that appear in the text
        - update.is_private (bool): Optional. True, if the sender and gift text are shown only to the gift receiver; otherwise, everyone will be able to see them
        - update.is_saved (bool): Optional. True, if the gift is displayed on the account's profile page; for gifts received on behalf of business accounts only
        - update.can_be_upgraded (bool): Optional. True, if the gift can be upgraded to a unique gift; for gifts received on behalf of business accounts only
        - update.was_refunded (bool): Optional. True, if the gift was refunded and isn't available anymore
        - update.convert_star_count (int): Optional. Number of Telegram Stars that can be claimed by the receiver instead of the gift; omitted if the gift cannot be converted to Telegram Stars
        - update.prepaid_upgrade_star_count (int): Optional. Number of Telegram Stars that were paid by the sender for the ability to upgrade the gift
        """
        # Example implementation
        # Implement your handler logic here
        pass
