from surfgram.types import InlineQuery
from typing import Callable


class ExampleInlineQuery(InlineQuery):
    """Example implementation of InlineQuery handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_inline_query",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the InlineQuery event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.id (str): Unique identifier for this query
        - update.from (User): Sender
        - update.query (str): Text of the query (up to 256 characters)
        - update.offset (str): Offset of the results to be returned, can be controlled by the bot
        - update.chat_type (str): Optional. Type of the chat from which the inline query was sent. Can be either "sender" for a private chat with the inline query sender, "private", "group", "supergroup", or "channel". The chat type should be always known for requests sent from official clients and most third-party clients, unless the request was sent from a secret chat
        - update.location (Location): Optional. Sender location, only for bots that request user location
        """
        # Example implementation
        # Implement your handler logic here
        pass
