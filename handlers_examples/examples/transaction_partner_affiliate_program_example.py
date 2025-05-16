from surfgram.types import TransactionPartnerAffiliateProgram
from typing import Callable


class ExampleTransactionPartnerAffiliateProgram(TransactionPartnerAffiliateProgram):
    """Example implementation of TransactionPartnerAffiliateProgram handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_transaction_partner_affiliate_program",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the TransactionPartnerAffiliateProgram event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the transaction partner, always "affiliate_program"
        - update.sponsor_user (User): Optional. Information about the bot that sponsored the affiliate program
        - update.commission_per_mille (int): The number of Telegram Stars received by the bot for each 1000 Telegram Stars received by the affiliate program sponsor from referred users
        """
        # Example implementation
        # Implement your handler logic here
        pass
