from surfgram.types import ChatMemberOwner
from typing import Callable


class ExampleChatMemberOwner(ChatMemberOwner):
    """Example implementation of ChatMemberOwner handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_chat_member_owner",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the ChatMemberOwner event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.status (str): The member's status in the chat, always "creator"
        - update.user (User): Information about the user
        - update.is_anonymous (bool): True, if the user's presence in the chat is hidden
        - update.custom_title (str): Optional. Custom title for this user
        """
        # Example implementation
        # Implement your handler logic here
        pass
