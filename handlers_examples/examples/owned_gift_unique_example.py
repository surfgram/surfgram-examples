from surfgram.types import OwnedGiftUnique
from typing import Callable


class ExampleOwnedGiftUnique(OwnedGiftUnique):
    """Example implementation of OwnedGiftUnique handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_owned_gift_unique",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the OwnedGiftUnique event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the gift, always "unique"
        - update.gift (UniqueGift): Information about the unique gift
        - update.owned_gift_id (str): Optional. Unique identifier of the received gift for the bot; for gifts received on behalf of business accounts only
        - update.sender_user (User): Optional. Sender of the gift if it is a known user
        - update.send_date (int): Date the gift was sent in Unix time
        - update.is_saved (bool): Optional. True, if the gift is displayed on the account's profile page; for gifts received on behalf of business accounts only
        - update.can_be_transferred (bool): Optional. True, if the gift can be transferred to another owner; for gifts received on behalf of business accounts only
        - update.transfer_star_count (int): Optional. Number of Telegram Stars that must be paid to transfer the gift; omitted if the bot cannot transfer the gift
        """
        # Example implementation
        # Implement your handler logic here
        pass
