from surfgram.types import User
from typing import Callable


class ExampleUser(User):
    """Example implementation of User handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_user",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the User event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.id (int): Unique identifier for this user or bot. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier.
        - update.is_bot (bool): True, if this user is a bot
        - update.first_name (str): User's or bot's first name
        - update.last_name (str): Optional. User's or bot's last name
        - update.username (str): Optional. User's or bot's username
        - update.language_code (str): Optional. IETF language tag of the user's language
        - update.is_premium (bool): Optional. True, if this user is a Telegram Premium user
        - update.added_to_attachment_menu (bool): Optional. True, if this user added the bot to the attachment menu
        - update.can_join_groups (bool): Optional. True, if the bot can be invited to groups. Returned only in getMe.
        - update.can_read_all_group_messages (bool): Optional. True, if privacy mode is disabled for the bot. Returned only in getMe.
        - update.supports_inline_queries (bool): Optional. True, if the bot supports inline queries. Returned only in getMe.
        - update.can_connect_to_business (bool): Optional. True, if the bot can be connected to a Telegram Business account to receive its messages. Returned only in getMe.
        - update.has_main_web_app (bool): Optional. True, if the bot has a main Web App. Returned only in getMe.
        """
        # Example implementation
        # Implement your handler logic here
        pass
