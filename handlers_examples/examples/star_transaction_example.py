from surfgram.types import StarTransaction
from typing import Callable


class ExampleStarTransaction(StarTransaction):
    """Example implementation of StarTransaction handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_star_transaction",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the StarTransaction event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.id (str): Unique identifier of the transaction. Coincides with the identifier of the original transaction for refund transactions. Coincides with SuccessfulPayment.telegram_payment_charge_id for successful incoming payments from users.
        - update.amount (int): Integer amount of Telegram Stars transferred by the transaction
        - update.nanostar_amount (int): Optional. The number of 1/1000000000 shares of Telegram Stars transferred by the transaction; from 0 to 999999999
        - update.date (int): Date the transaction was created in Unix time
        - update.source (TransactionPartner): Optional. Source of an incoming transaction (e.g., a user purchasing goods or services, Fragment refunding a failed withdrawal). Only for incoming transactions
        - update.receiver (TransactionPartner): Optional. Receiver of an outgoing transaction (e.g., a user for a purchase refund, Fragment for a withdrawal). Only for outgoing transactions
        """
        # Example implementation
        # Implement your handler logic here
        pass
