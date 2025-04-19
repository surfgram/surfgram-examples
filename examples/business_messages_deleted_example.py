from surfgram.types import BusinessMessagesDeleted
from typing import Callable


class ExampleBusinessMessagesDeleted(BusinessMessagesDeleted):
    """Example implementation of BusinessMessagesDeleted handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_business_messages_deleted",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the BusinessMessagesDeleted event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.business_connection_id (str): Unique identifier of the business connection
        - update.chat (Chat): Information about a chat in the business account. The bot may not have access to the chat or the corresponding user.
        - update.message_ids (List[int]): The list of identifiers of deleted messages in the chat of the business account
        """
        # Example implementation
        # Implement your handler logic here
        pass
