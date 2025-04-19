from surfgram.types import TransactionPartnerChat
from typing import Callable


class ExampleTransactionPartnerChat(TransactionPartnerChat):
    """Example implementation of TransactionPartnerChat handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_transaction_partner_chat",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the TransactionPartnerChat event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the transaction partner, always "chat"
        - update.chat (Chat): Information about the chat
        - update.gift (Gift): Optional. The gift sent to the chat by the bot
        """
        # Example implementation
        # Implement your handler logic here
        pass
