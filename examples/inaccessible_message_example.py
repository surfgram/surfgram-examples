from surfgram.types import InaccessibleMessage
from typing import Callable


class ExampleInaccessibleMessage(InaccessibleMessage):
    """Example implementation of InaccessibleMessage handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_inaccessible_message",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the InaccessibleMessage event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.chat (Chat): Chat the message belonged to
        - update.message_id (int): Unique message identifier inside the chat
        - update.date (int): Always 0. The field can be used to differentiate regular and inaccessible messages.
        """
        # Example implementation
        # Implement your handler logic here
        pass
