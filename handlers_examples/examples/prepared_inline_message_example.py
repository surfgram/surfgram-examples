from surfgram.types import PreparedInlineMessage
from typing import Callable


class ExamplePreparedInlineMessage(PreparedInlineMessage):
    """Example implementation of PreparedInlineMessage handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_prepared_inline_message",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the PreparedInlineMessage event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.id (str): Unique identifier of the prepared message
        - update.expiration_date (int): Expiration date of the prepared message, in Unix time. Expired prepared messages can no longer be used
        """
        # Example implementation
        # Implement your handler logic here
        pass
