from surfgram.types import ChatShared
from typing import Callable


class ExampleChatShared(ChatShared):
    """Example implementation of ChatShared handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_chat_shared",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the ChatShared event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.request_id (int): Identifier of the request
        - update.chat_id (int): Identifier of the shared chat. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier. The bot may not have access to the chat and could be unable to use this identifier, unless the chat is already known to the bot by some other means.
        - update.title (str): Optional. Title of the chat, if the title was requested by the bot.
        - update.username (str): Optional. Username of the chat, if the username was requested by the bot and available.
        - update.photo (List[PhotoSize]): Optional. Available sizes of the chat photo, if the photo was requested by the bot
        """
        # Example implementation
        # Implement your handler logic here
        pass
