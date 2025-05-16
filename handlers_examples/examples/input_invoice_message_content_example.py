from surfgram.types import InputInvoiceMessageContent
from typing import Callable


class ExampleInputInvoiceMessageContent(InputInvoiceMessageContent):
    """Example implementation of InputInvoiceMessageContent handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_input_invoice_message_content",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the InputInvoiceMessageContent event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.title (str): Product name, 1-32 characters
        - update.description (str): Product description, 1-255 characters
        - update.payload (str): Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use it for your internal processes.
        - update.provider_token (str): Optional. Payment provider token, obtained via @BotFather. Pass an empty string for payments in Telegram Stars.
        - update.currency (str): Three-letter ISO 4217 currency code, see more on currencies. Pass "XTR" for payments in Telegram Stars.
        - update.prices (List[LabeledPrice]): Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.). Must contain exactly one item for payments in Telegram Stars.
        - update.max_tip_amount (int): Optional. The maximum accepted amount for tips in the smallest units of the currency (integer, not float/double). For example, for a maximum tip of US$ 1.45 pass max_tip_amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). Defaults to 0. Not supported for payments in Telegram Stars.
        - update.suggested_tip_amounts (List[int]): Optional. A JSON-serialized array of suggested amounts of tip in the smallest units of the currency (integer, not float/double). At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed max_tip_amount.
        - update.provider_data (str): Optional. A JSON-serialized object for data about the invoice, which will be shared with the payment provider. A detailed description of the required fields should be provided by the payment provider.
        - update.photo_url (str): Optional. URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service.
        - update.photo_size (int): Optional. Photo size in bytes
        - update.photo_width (int): Optional. Photo width
        - update.photo_height (int): Optional. Photo height
        - update.need_name (bool): Optional. Pass True if you require the user's full name to complete the order. Ignored for payments in Telegram Stars.
        - update.need_phone_number (bool): Optional. Pass True if you require the user's phone number to complete the order. Ignored for payments in Telegram Stars.
        - update.need_email (bool): Optional. Pass True if you require the user's email address to complete the order. Ignored for payments in Telegram Stars.
        - update.need_shipping_address (bool): Optional. Pass True if you require the user's shipping address to complete the order. Ignored for payments in Telegram Stars.
        - update.send_phone_number_to_provider (bool): Optional. Pass True if the user's phone number should be sent to the provider. Ignored for payments in Telegram Stars.
        - update.send_email_to_provider (bool): Optional. Pass True if the user's email address should be sent to the provider. Ignored for payments in Telegram Stars.
        - update.is_flexible (bool): Optional. Pass True if the final price depends on the shipping method. Ignored for payments in Telegram Stars.
        """
        # Example implementation
        # Implement your handler logic here
        pass
