from surfgram.types import KeyboardButtonRequestChat
from typing import Callable


class ExampleKeyboardButtonRequestChat(KeyboardButtonRequestChat):
    """Example implementation of KeyboardButtonRequestChat handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_keyboard_button_request_chat",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the KeyboardButtonRequestChat event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.request_id (int): Signed 32-bit identifier of the request, which will be received back in the ChatShared object. Must be unique within the message
        - update.chat_is_channel (bool): Pass True to request a channel chat, pass False to request a group or a supergroup chat.
        - update.chat_is_forum (bool): Optional. Pass True to request a forum supergroup, pass False to request a non-forum chat. If not specified, no additional restrictions are applied.
        - update.chat_has_username (bool): Optional. Pass True to request a supergroup or a channel with a username, pass False to request a chat without a username. If not specified, no additional restrictions are applied.
        - update.chat_is_created (bool): Optional. Pass True to request a chat owned by the user. Otherwise, no additional restrictions are applied.
        - update.user_administrator_rights (Union[ChatAdministrat, Rights]): Optional. A JSON-serialized object listing the required administrator rights of the user in the chat. The rights must be a superset of bot_administrator_rights. If not specified, no additional restrictions are applied.
        - update.bot_administrator_rights (Union[ChatAdministrat, Rights]): Optional. A JSON-serialized object listing the required administrator rights of the bot in the chat. The rights must be a subset of user_administrator_rights. If not specified, no additional restrictions are applied.
        - update.bot_is_member (bool): Optional. Pass True to request a chat with the bot as a member. Otherwise, no additional restrictions are applied.
        - update.request_title (bool): Optional. Pass True to request the chat's title
        - update.request_username (bool): Optional. Pass True to request the chat's username
        - update.request_photo (bool): Optional. Pass True to request the chat's photo
        """
        # Example implementation
        # Implement your handler logic here
        pass
