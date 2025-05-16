from surfgram.types import InlineQueryResultGif
from typing import Callable


class ExampleInlineQueryResultGif(InlineQueryResultGif):
    """Example implementation of InlineQueryResultGif handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_inline_query_result_gif",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the InlineQueryResultGif event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the result, must be gif
        - update.id (str): Unique identifier for this result, 1-64 bytes
        - update.gif_url (str): A valid URL for the GIF file
        - update.gif_width (int): Optional. Width of the GIF
        - update.gif_height (int): Optional. Height of the GIF
        - update.gif_duration (int): Optional. Duration of the GIF in seconds
        - update.thumbnail_url (str): URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result
        - update.thumbnail_mime_type (str): Optional. MIME type of the thumbnail, must be one of "image/jpeg", "image/gif", or "video/mp4". Defaults to "image/jpeg"
        - update.title (str): Optional. Title for the result
        - update.caption (str): Optional. Caption of the GIF file to be sent, 0-1024 characters after entities parsing
        - update.parse_mode (str): Optional. Mode for parsing entities in the caption. See formatting options for more details.
        - update.caption_entities (List[MessageEntity]): Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
        - update.show_caption_above_media (bool): Optional. Pass True, if the caption must be shown above the message media
        - update.reply_markup (InlineKeyboardMarkup): Optional. Inline keyboard attached to the message
        - update.input_message_content (InputMessageContent): Optional. Content of the message to be sent instead of the GIF animation
        - update.type (str): Type of the result, must be mpeg4_gif
        - update.id (str): Unique identifier for this result, 1-64 bytes
        - update.mpeg4_url (str): A valid URL for the MPEG4 file
        - update.mpeg4_width (int): Optional. Video width
        - update.mpeg4_height (int): Optional. Video height
        - update.mpeg4_duration (int): Optional. Video duration in seconds
        - update.thumbnail_url (str): URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result
        - update.thumbnail_mime_type (str): Optional. MIME type of the thumbnail, must be one of "image/jpeg", "image/gif", or "video/mp4". Defaults to "image/jpeg"
        - update.title (str): Optional. Title for the result
        - update.caption (str): Optional. Caption of the MPEG-4 file to be sent, 0-1024 characters after entities parsing
        - update.parse_mode (str): Optional. Mode for parsing entities in the caption. See formatting options for more details.
        - update.caption_entities (List[MessageEntity]): Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
        - update.show_caption_above_media (bool): Optional. Pass True, if the caption must be shown above the message media
        - update.reply_markup (InlineKeyboardMarkup): Optional. Inline keyboard attached to the message
        - update.input_message_content (InputMessageContent): Optional. Content of the message to be sent instead of the video animation
        """
        # Example implementation
        # Implement your handler logic here
        pass
