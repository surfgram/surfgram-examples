from surfgram.types import SharedUser
from typing import Callable


class ExampleSharedUser(SharedUser):
    """Example implementation of SharedUser handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_shared_user",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the SharedUser event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.user_id (int): Identifier of the shared user. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so 64-bit integers or double-precision float types are safe for storing these identifiers. The bot may not have access to the user and could be unable to use this identifier, unless the user is already known to the bot by some other means.
        - update.first_name (str): Optional. First name of the user, if the name was requested by the bot
        - update.last_name (str): Optional. Last name of the user, if the name was requested by the bot
        - update.username (str): Optional. Username of the user, if the username was requested by the bot
        - update.photo (List[PhotoSize]): Optional. Available sizes of the chat photo, if the photo was requested by the bot
        """
        # Example implementation
        # Implement your handler logic here
        pass
