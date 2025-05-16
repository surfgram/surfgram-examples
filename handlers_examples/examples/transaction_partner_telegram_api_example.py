from surfgram.types import TransactionPartnerTelegramApi
from typing import Callable


class ExampleTransactionPartnerTelegramApi(TransactionPartnerTelegramApi):
    """Example implementation of TransactionPartnerTelegramApi handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_transaction_partner_telegram_api",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the TransactionPartnerTelegramApi event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the transaction partner, always "telegram_api"
        - update.request_count (int): The number of successful requests that exceeded regular limits and were therefore billed
        """
        # Example implementation
        # Implement your handler logic here
        pass
