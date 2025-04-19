from surfgram.types import InlineQueryResultArticle
from typing import Callable


class ExampleInlineQueryResultArticle(InlineQueryResultArticle):
    """Example implementation of InlineQueryResultArticle handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_inline_query_result_article",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the InlineQueryResultArticle event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the result, must be article
        - update.id (str): Unique identifier for this result, 1-64 Bytes
        - update.title (str): Title of the result
        - update.input_message_content (InputMessageContent): Content of the message to be sent
        - update.reply_markup (InlineKeyboardMarkup): Optional. Inline keyboard attached to the message
        - update.url (str): Optional. URL of the result
        - update.description (str): Optional. Short description of the result
        - update.thumbnail_url (str): Optional. Url of the thumbnail for the result
        - update.thumbnail_width (int): Optional. Thumbnail width
        - update.thumbnail_height (int): Optional. Thumbnail height
        """
        # Example implementation
        # Implement your handler logic here
        pass
