from surfgram.types import TransactionPartnerOther
from typing import Callable


class ExampleTransactionPartnerOther(TransactionPartnerOther):
    """Example implementation of TransactionPartnerOther handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_transaction_partner_other",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the TransactionPartnerOther event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the transaction partner, always "other"
        """
        # Example implementation
        # Implement your handler logic here
        pass
