from surfgram.types import ChatMemberBanned
from typing import Callable


class ExampleChatMemberBanned(ChatMemberBanned):
    """Example implementation of ChatMemberBanned handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_chat_member_banned",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the ChatMemberBanned event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.status (str): The member's status in the chat, always "kicked"
        - update.user (User): Information about the user
        - update.until_date (int): Date when restrictions will be lifted for this user; Unix time. If 0, then the user is banned forever
        """
        # Example implementation
        # Implement your handler logic here
        pass
