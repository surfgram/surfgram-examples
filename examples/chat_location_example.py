from surfgram.types import ChatLocation
from typing import Callable


class ExampleChatLocation(ChatLocation):
    """Example implementation of ChatLocation handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_chat_location",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the ChatLocation event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.location (Location): The location to which the supergroup is connected. Can't be a live location.
        - update.address (str): Location address; 1-64 characters, as defined by the chat owner
        """
        # Example implementation
        # Implement your handler logic here
        pass
