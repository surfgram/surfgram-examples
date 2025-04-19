from surfgram.types import ChatMemberLeft
from typing import Callable


class ExampleChatMemberLeft(ChatMemberLeft):
    """Example implementation of ChatMemberLeft handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_chat_member_left",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the ChatMemberLeft event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.status (str): The member's status in the chat, always "left"
        - update.user (User): Information about the user
        """
        # Example implementation
        # Implement your handler logic here
        pass
