from surfgram.types import Chat
from typing import Callable


class ExampleChat(Chat):
    """Example implementation of Chat handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_chat",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the Chat event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.id (int): Unique identifier for this chat. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
        - update.type (str): Type of the chat, can be either "private", "group", "supergroup" or "channel"
        - update.title (str): Optional. Title, for supergroups, channels and group chats
        - update.username (str): Optional. Username, for private chats, supergroups and channels if available
        - update.first_name (str): Optional. First name of the other party in a private chat
        - update.last_name (str): Optional. Last name of the other party in a private chat
        - update.is_forum (bool): Optional. True, if the supergroup chat is a forum (has topics enabled)
        """
        # Example implementation
        # Implement your handler logic here
        pass
