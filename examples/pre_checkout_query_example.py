from surfgram.types import PreCheckoutQuery
from typing import Callable


class ExamplePreCheckoutQuery(PreCheckoutQuery):
    """Example implementation of PreCheckoutQuery handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_pre_checkout_query",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the PreCheckoutQuery event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.id (str): Unique query identifier
        - update.from (User): User who sent the query
        - update.currency (str): Three-letter ISO 4217 currency code, or "XTR" for payments in Telegram Stars
        - update.total_amount (int): Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
        - update.invoice_payload (str): Bot-specified invoice payload
        - update.shipping_option_id (str): Optional. Identifier of the shipping option chosen by the user
        - update.order_info (OrderInfo): Optional. Order information provided by the user
        """
        # Example implementation
        # Implement your handler logic here
        pass
