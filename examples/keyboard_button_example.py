from surfgram.types import KeyboardButton
from typing import Callable


class ExampleKeyboardButton(KeyboardButton):
    """Example implementation of KeyboardButton handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_keyboard_button",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the KeyboardButton event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.text (str): Text of the button. If none of the optional fields are used, it will be sent as a message when the button is pressed
        - update.request_users (KeyboardButtonRequestUsers): Optional. If specified, pressing the button will open a list of suitable users. Identifiers of selected users will be sent to the bot in a "users_shared" service message. Available in private chats only.
        - update.request_chat (KeyboardButtonRequestChat): Optional. If specified, pressing the button will open a list of suitable chats. Tapping on a chat will send its identifier to the bot in a "chat_shared" service message. Available in private chats only.
        - update.request_contact (bool): Optional. If True, the user's phone number will be sent as a contact when the button is pressed. Available in private chats only.
        - update.request_location (bool): Optional. If True, the user's current location will be sent when the button is pressed. Available in private chats only.
        - update.request_poll (KeyboardButtonPollType): Optional. If specified, the user will be asked to create a poll and send it to the bot when the button is pressed. Available in private chats only.
        - update.web_app (WebAppInfo): Optional. If specified, the described Web App will be launched when the button is pressed. The Web App will be able to send a "web_app_data" service message. Available in private chats only.
        """
        # Example implementation
        # Implement your handler logic here
        pass
