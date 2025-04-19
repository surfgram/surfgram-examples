from surfgram.types import ChatMemberMember
from typing import Callable


class ExampleChatMemberMember(ChatMemberMember):
    """Example implementation of ChatMemberMember handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_chat_member_member",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the ChatMemberMember event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.status (str): The member's status in the chat, always "member"
        - update.user (User): Information about the user
        - update.until_date (int): Optional. Date when the user's subscription will expire; Unix time
        """
        # Example implementation
        # Implement your handler logic here
        pass
