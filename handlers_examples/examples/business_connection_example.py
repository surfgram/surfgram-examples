from surfgram.types import BusinessConnection
from typing import Callable


class ExampleBusinessConnection(BusinessConnection):
    """Example implementation of BusinessConnection handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_business_connection",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the BusinessConnection event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.id (str): Unique identifier of the business connection
        - update.user (User): Business account user that created the business connection
        - update.user_chat_id (int): Identifier of a private chat with the user who created the business connection. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier.
        - update.date (int): Date the connection was established in Unix time
        - update.rights (BusinessBotRights): Optional. Rights of the business bot
        - update.is_enabled (bool): True, if the connection is active
        """
        # Example implementation
        # Implement your handler logic here
        pass
