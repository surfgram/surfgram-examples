from surfgram.types import KeyboardButtonRequestUsers
from typing import Callable


class ExampleKeyboardButtonRequestUsers(KeyboardButtonRequestUsers):
    """Example implementation of KeyboardButtonRequestUsers handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_keyboard_button_request_users",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the KeyboardButtonRequestUsers event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.request_id (int): Signed 32-bit identifier of the request that will be received back in the UsersShared object. Must be unique within the message
        - update.user_is_bot (bool): Optional. Pass True to request bots, pass False to request regular users. If not specified, no additional restrictions are applied.
        - update.user_is_premium (bool): Optional. Pass True to request premium users, pass False to request non-premium users. If not specified, no additional restrictions are applied.
        - update.max_quantity (int): Optional. The maximum number of users to be selected; 1-10. Defaults to 1.
        - update.request_name (bool): Optional. Pass True to request the users' first and last names
        - update.request_username (bool): Optional. Pass True to request the users' usernames
        - update.request_photo (bool): Optional. Pass True to request the users' photos
        """
        # Example implementation
        # Implement your handler logic here
        pass
