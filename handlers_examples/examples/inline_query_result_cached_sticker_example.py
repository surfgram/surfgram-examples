from surfgram.types import InlineQueryResultCachedSticker
from typing import Callable


class ExampleInlineQueryResultCachedSticker(InlineQueryResultCachedSticker):
    """Example implementation of InlineQueryResultCachedSticker handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_inline_query_result_cached_sticker",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the InlineQueryResultCachedSticker event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the result, must be sticker
        - update.id (str): Unique identifier for this result, 1-64 bytes
        - update.sticker_file_id (str): A valid file identifier of the sticker
        - update.reply_markup (InlineKeyboardMarkup): Optional. Inline keyboard attached to the message
        - update.input_message_content (InputMessageContent): Optional. Content of the message to be sent instead of the sticker
        """
        # Example implementation
        # Implement your handler logic here
        pass
