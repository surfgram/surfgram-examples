from surfgram.types import InlineQueryResultDocument
from typing import Callable


class ExampleInlineQueryResultDocument(InlineQueryResultDocument):
    """Example implementation of InlineQueryResultDocument handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_inline_query_result_document",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the InlineQueryResultDocument event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the result, must be document
        - update.id (str): Unique identifier for this result, 1-64 bytes
        - update.title (str): Title for the result
        - update.caption (str): Optional. Caption of the document to be sent, 0-1024 characters after entities parsing
        - update.parse_mode (str): Optional. Mode for parsing entities in the document caption. See formatting options for more details.
        - update.caption_entities (List[MessageEntity]): Optional. List of special entities that appear in the caption, which can be specified instead of parse_mode
        - update.document_url (str): A valid URL for the file
        - update.mime_type (str): MIME type of the content of the file, either "application/pdf" or "application/zip"
        - update.description (str): Optional. Short description of the result
        - update.reply_markup (InlineKeyboardMarkup): Optional. Inline keyboard attached to the message
        - update.input_message_content (InputMessageContent): Optional. Content of the message to be sent instead of the file
        - update.thumbnail_url (str): Optional. URL of the thumbnail (JPEG only) for the file
        - update.thumbnail_width (int): Optional. Thumbnail width
        - update.thumbnail_height (int): Optional. Thumbnail height
        """
        # Example implementation
        # Implement your handler logic here
        pass
