from surfgram.types import ChatBoostSourcePremium
from typing import Callable


class ExampleChatBoostSourcePremium(ChatBoostSourcePremium):
    """Example implementation of ChatBoostSourcePremium handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_chat_boost_source_premium",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the ChatBoostSourcePremium event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.source (str): Source of the boost, always "premium"
        - update.user (User): User that boosted the chat
        """
        # Example implementation
        # Implement your handler logic here
        pass
