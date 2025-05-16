from surfgram.types import MessageOriginChannel
from typing import Callable


class ExampleMessageOriginChannel(MessageOriginChannel):
    """Example implementation of MessageOriginChannel handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_message_origin_channel",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the MessageOriginChannel event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the message origin, always "channel"
        - update.date (int): Date the message was sent originally in Unix time
        - update.chat (Chat): Channel chat to which the message was originally sent
        - update.message_id (int): Unique message identifier inside the chat
        - update.author_signature (str): Optional. Signature of the original post author
        """
        # Example implementation
        # Implement your handler logic here
        pass
