from surfgram.types import InlineQueryResultPhoto
from typing import Callable


class ExampleInlineQueryResultPhoto(InlineQueryResultPhoto):
    """Example implementation of InlineQueryResultPhoto handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_inline_query_result_photo",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the InlineQueryResultPhoto event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the result, must be photo
        - update.id (str): Unique identifier for this result, 1-64 bytes
        - update.photo_url (str): A valid URL of the photo. Photo must be in JPEG format. Photo size must not exceed 5MB
        - update.thumbnail_url (str): URL of the thumbnail for the photo
        - update.photo_width (int): Optional. Width of the photo
        - update.photo_height (int): Optional. Height of the photo
        - update.title (str): Optional. Title for the result
        - update.description (str): Optional. Short description of the result
        - update.caption (str): Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing
        - update.parse_mode (str): Optional. Mode for parsing entities in the photo caption. See formatting options for more details.
        - update.caption_entities (List[MessageEntity]): Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
        - update.show_caption_above_media (bool): Optional. Pass True, if the caption must be shown above the message media
        - update.reply_markup (InlineKeyboardMarkup): Optional. Inline keyboard attached to the message
        - update.input_message_content (InputMessageContent): Optional. Content of the message to be sent instead of the photo
        """
        # Example implementation
        # Implement your handler logic here
        pass
