from surfgram.types import InlineQueryResultContact
from typing import Callable


class ExampleInlineQueryResultContact(InlineQueryResultContact):
    """Example implementation of InlineQueryResultContact handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_inline_query_result_contact",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the InlineQueryResultContact event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the result, must be contact
        - update.id (str): Unique identifier for this result, 1-64 Bytes
        - update.phone_number (str): Contact's phone number
        - update.first_name (str): Contact's first name
        - update.last_name (str): Optional. Contact's last name
        - update.vcard (str): Optional. Additional data about the contact in the form of a vCard, 0-2048 bytes
        - update.reply_markup (InlineKeyboardMarkup): Optional. Inline keyboard attached to the message
        - update.input_message_content (InputMessageContent): Optional. Content of the message to be sent instead of the contact
        - update.thumbnail_url (str): Optional. Url of the thumbnail for the result
        - update.thumbnail_width (int): Optional. Thumbnail width
        - update.thumbnail_height (int): Optional. Thumbnail height
        """
        # Example implementation
        # Implement your handler logic here
        pass
