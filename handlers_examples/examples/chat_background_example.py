from surfgram.types import ChatBackground
from typing import Callable


class ExampleChatBackground(ChatBackground):
    """Example implementation of ChatBackground handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_chat_background",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the ChatBackground event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (BackgroundType): Type of the background
        """
        # Example implementation
        # Implement your handler logic here
        pass
