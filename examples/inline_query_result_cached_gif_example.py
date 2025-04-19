from surfgram.types import InlineQueryResultCachedGif
from typing import Callable


class ExampleInlineQueryResultCachedGif(InlineQueryResultCachedGif):
    """Example implementation of InlineQueryResultCachedGif handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_inline_query_result_cached_gif",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the InlineQueryResultCachedGif event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the result, must be gif
        - update.id (str): Unique identifier for this result, 1-64 bytes
        - update.gif_file_id (str): A valid file identifier for the GIF file
        - update.title (str): Optional. Title for the result
        - update.caption (str): Optional. Caption of the GIF file to be sent, 0-1024 characters after entities parsing
        - update.parse_mode (str): Optional. Mode for parsing entities in the caption. See formatting options for more details.
        - update.caption_entities (List[MessageEntity]): Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
        - update.show_caption_above_media (bool): Optional. Pass True, if the caption must be shown above the message media
        - update.reply_markup (InlineKeyboardMarkup): Optional. Inline keyboard attached to the message
        - update.input_message_content (InputMessageContent): Optional. Content of the message to be sent instead of the GIF animation
        - update.type (str): Type of the result, must be mpeg4_gif
        - update.id (str): Unique identifier for this result, 1-64 bytes
        - update.mpeg4_file_id (str): A valid file identifier for the MPEG4 file
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
