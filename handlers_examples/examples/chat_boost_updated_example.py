from surfgram.types import ChatBoostUpdated
from typing import Callable


class ExampleChatBoostUpdated(ChatBoostUpdated):
    """Example implementation of ChatBoostUpdated handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_chat_boost_updated",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the ChatBoostUpdated event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.chat (Chat): Chat which was boosted
        - update.boost (ChatBoost): Information about the chat boost
        """
        # Example implementation
        # Implement your handler logic here
        pass
