from surfgram.types import RefundedPayment
from typing import Callable


class ExampleRefundedPayment(RefundedPayment):
    """Example implementation of RefundedPayment handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_refunded_payment",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the RefundedPayment event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.currency (str): Three-letter ISO 4217 currency code, or "XTR" for payments in Telegram Stars. Currently, always "XTR"
        - update.total_amount (int): Total refunded price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45, total_amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
        - update.invoice_payload (str): Bot-specified invoice payload
        - update.telegram_payment_charge_id (str): Telegram payment identifier
        - update.provider_payment_charge_id (str): Optional. Provider payment identifier
        """
        # Example implementation
        # Implement your handler logic here
        pass
