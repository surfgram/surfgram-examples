from surfgram.types import SuccessfulPayment
from typing import Callable


class ExampleSuccessfulPayment(SuccessfulPayment):
    """Example implementation of SuccessfulPayment handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_successful_payment",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the SuccessfulPayment event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.currency (str): Three-letter ISO 4217 currency code, or "XTR" for payments in Telegram Stars
        - update.total_amount (int): Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
        - update.invoice_payload (str): Bot-specified invoice payload
        - update.subscription_expiration_date (int): Optional. Expiration date of the subscription, in Unix time; for recurring payments only
        - update.is_recurring (bool): Optional. True, if the payment is a recurring payment for a subscription
        - update.is_first_recurring (bool): Optional. True, if the payment is the first payment for a subscription
        - update.shipping_option_id (str): Optional. Identifier of the shipping option chosen by the user
        - update.order_info (OrderInfo): Optional. Order information provided by the user
        - update.telegram_payment_charge_id (str): Telegram payment identifier
        - update.provider_payment_charge_id (str): Provider payment identifier
        """
        # Example implementation
        # Implement your handler logic here
        pass
