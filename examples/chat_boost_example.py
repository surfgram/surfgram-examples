from surfgram.types import ChatBoost
from typing import Callable


class ExampleChatBoost(ChatBoost):
    """Example implementation of ChatBoost handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_chat_boost",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the ChatBoost event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.boost_id (str): Unique identifier of the boost
        - update.add_date (int): Point in time (Unix timestamp) when the chat was boosted
        - update.expiration_date (int): Point in time (Unix timestamp) when the boost will automatically expire, unless the booster's Telegram Premium subscription is prolonged
        - update.source (ChatBoostSource): Source of the added boost
        """
        # Example implementation
        # Implement your handler logic here
        pass
