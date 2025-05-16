from surfgram.types import ResponseParameters
from typing import Callable


class ExampleResponseParameters(ResponseParameters):
    """Example implementation of ResponseParameters handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_response_parameters",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the ResponseParameters event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.migrate_to_chat_id (int): Optional. The group has been migrated to a supergroup with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
        - update.retry_after (int): Optional. In case of exceeding flood control, the number of seconds left to wait before the request can be repeated
        """
        # Example implementation
        # Implement your handler logic here
        pass
