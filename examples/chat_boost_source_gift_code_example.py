from surfgram.types import ChatBoostSourceGiftCode
from typing import Callable


class ExampleChatBoostSourceGiftCode(ChatBoostSourceGiftCode):
    """Example implementation of ChatBoostSourceGiftCode handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_chat_boost_source_gift_code",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the ChatBoostSourceGiftCode event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.source (str): Source of the boost, always "gift_code"
        - update.user (User): User for which the gift code was created
        """
        # Example implementation
        # Implement your handler logic here
        pass
