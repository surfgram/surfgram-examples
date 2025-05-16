from surfgram.types import MessageOriginUser
from typing import Callable


class ExampleMessageOriginUser(MessageOriginUser):
    """Example implementation of MessageOriginUser handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_message_origin_user",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the MessageOriginUser event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the message origin, always "user"
        - update.date (int): Date the message was sent originally in Unix time
        - update.sender_user (User): User that sent the message originally
        """
        # Example implementation
        # Implement your handler logic here
        pass
