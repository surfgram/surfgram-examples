from surfgram.types import ReplyParameters
from typing import Callable


class ExampleReplyParameters(ReplyParameters):
    """Example implementation of ReplyParameters handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_reply_parameters",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the ReplyParameters event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.message_id (int): Identifier of the message that will be replied to in the current chat, or in the chat chat_id if it is specified
        - update.chat_id (Union[int, str]): Optional. If the message to be replied to is from a different chat, unique identifier for the chat or username of the channel (in the format @channelusername). Not supported for messages sent on behalf of a business account.
        - update.allow_sending_without_reply (bool): Optional. Pass True if the message should be sent even if the specified message to be replied to is not found. Always False for replies in another chat or forum topic. Always True for messages sent on behalf of a business account.
        - update.quote (str): Optional. Quoted part of the message to be replied to; 0-1024 characters after entities parsing. The quote must be an exact substring of the message to be replied to, including bold, italic, underline, strikethrough, spoiler, and custom_emoji entities. The message will fail to send if the quote isn't found in the original message.
        - update.quote_parse_mode (str): Optional. Mode for parsing entities in the quote. See formatting options for more details.
        - update.quote_entities (List[MessageEntity]): Optional. A JSON-serialized list of special entities that appear in the quote. It can be specified instead of quote_parse_mode.
        - update.quote_position (int): Optional. Position of the quote in the original message in UTF-16 code units
        """
        # Example implementation
        # Implement your handler logic here
        pass
