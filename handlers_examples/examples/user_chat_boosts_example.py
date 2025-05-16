from surfgram.types import UserChatBoosts
from typing import Callable


class ExampleUserChatBoosts(UserChatBoosts):
    """Example implementation of UserChatBoosts handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_user_chat_boosts",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the UserChatBoosts event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.boosts (List[ChatBoost]): The list of boosts added to the chat by the user
        """
        # Example implementation
        # Implement your handler logic here
        pass
