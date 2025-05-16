from surfgram.types import TextQuote
from typing import Callable


class ExampleTextQuote(TextQuote):
    """Example implementation of TextQuote handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_text_quote",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the TextQuote event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.text (str): Text of the quoted part of a message that is replied to by the given message
        - update.entities (List[MessageEntity]): Optional. Special entities that appear in the quote. Currently, only bold, italic, underline, strikethrough, spoiler, and custom_emoji entities are kept in quotes.
        - update.position (int): Approximate quote position in the original message in UTF-16 code units as specified by the sender
        - update.is_manual (bool): Optional. True, if the quote was chosen manually by the message sender. Otherwise, the quote was added automatically by the server.
        """
        # Example implementation
        # Implement your handler logic here
        pass
