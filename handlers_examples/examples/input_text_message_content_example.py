from surfgram.types import InputTextMessageContent
from typing import Callable


class ExampleInputTextMessageContent(InputTextMessageContent):
    """Example implementation of InputTextMessageContent handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_input_text_message_content",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the InputTextMessageContent event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.message_text (str): Text of the message to be sent, 1-4096 characters
        - update.parse_mode (str): Optional. Mode for parsing entities in the message text. See formatting options for more details.
        - update.entities (List[MessageEntity]): Optional. List of special entities that appear in message text, which can be specified instead of parse_mode
        - update.link_preview_options (LinkPreviewOptions): Optional. Link preview generation options for the message
        """
        # Example implementation
        # Implement your handler logic here
        pass
