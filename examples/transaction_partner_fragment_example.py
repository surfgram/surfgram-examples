from surfgram.types import TransactionPartnerFragment
from typing import Callable


class ExampleTransactionPartnerFragment(TransactionPartnerFragment):
    """Example implementation of TransactionPartnerFragment handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_transaction_partner_fragment",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the TransactionPartnerFragment event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the transaction partner, always "fragment"
        - update.withdrawal_state (RevenueWithdrawalState): Optional. State of the transaction if the transaction is outgoing
        """
        # Example implementation
        # Implement your handler logic here
        pass
