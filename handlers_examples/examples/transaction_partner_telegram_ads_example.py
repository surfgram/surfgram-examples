from surfgram.types import TransactionPartnerTelegramAds
from typing import Callable


class ExampleTransactionPartnerTelegramAds(TransactionPartnerTelegramAds):
    """Example implementation of TransactionPartnerTelegramAds handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_transaction_partner_telegram_ads",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the TransactionPartnerTelegramAds event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the transaction partner, always "telegram_ads"
        """
        # Example implementation
        # Implement your handler logic here
        pass
