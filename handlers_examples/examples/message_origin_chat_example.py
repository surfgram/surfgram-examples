from surfgram.types import MessageOriginChat
from typing import Callable


class ExampleMessageOriginChat(MessageOriginChat):
    """Example implementation of MessageOriginChat handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_message_origin_chat",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the MessageOriginChat event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the message origin, always "chat"
        - update.date (int): Date the message was sent originally in Unix time
        - update.sender_chat (Chat): Chat that sent the message originally
        - update.author_signature (str): Optional. For messages originally sent by an anonymous chat administrator, original message author signature
        """
        # Example implementation
        # Implement your handler logic here
        pass
