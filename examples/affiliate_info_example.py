from surfgram.types import AffiliateInfo
from typing import Callable


class ExampleAffiliateInfo(AffiliateInfo):
    """Example implementation of AffiliateInfo handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_affiliate_info",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the AffiliateInfo event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.affiliate_user (User): Optional. The bot or the user that received an affiliate commission if it was received by a bot or a user
        - update.affiliate_chat (Chat): Optional. The chat that received an affiliate commission if it was received by a chat
        - update.commission_per_mille (int): The number of Telegram Stars received by the affiliate for each 1000 Telegram Stars received by the bot from referred users
        - update.amount (int): Integer amount of Telegram Stars received by the affiliate from the transaction, rounded to 0; can be negative for refunds
        - update.nanostar_amount (int): Optional. The number of 1/1000000000 shares of Telegram Stars received by the affiliate; from -999999999 to 999999999; can be negative for refunds
        """
        # Example implementation
        # Implement your handler logic here
        pass
