from surfgram.types import ChatBoostAdded
from typing import Callable


class ExampleChatBoostAdded(ChatBoostAdded):
    """Example implementation of ChatBoostAdded handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_chat_boost_added",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the ChatBoostAdded event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.boost_count (int): Number of boosts added by the user
        """
        # Example implementation
        # Implement your handler logic here
        pass
