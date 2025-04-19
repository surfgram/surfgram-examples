from surfgram.types import ChatBoostRemoved
from typing import Callable


class ExampleChatBoostRemoved(ChatBoostRemoved):
    """Example implementation of ChatBoostRemoved handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_chat_boost_removed",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the ChatBoostRemoved event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.chat (Chat): Chat which was boosted
        - update.boost_id (str): Unique identifier of the boost
        - update.remove_date (int): Point in time (Unix timestamp) when the boost was removed
        - update.source (ChatBoostSource): Source of the removed boost
        """
        # Example implementation
        # Implement your handler logic here
        pass
