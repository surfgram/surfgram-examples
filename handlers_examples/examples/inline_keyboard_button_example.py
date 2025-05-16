from surfgram.types import InlineKeyboardButton
from typing import Callable


class ExampleInlineKeyboardButton(InlineKeyboardButton):
    """Example implementation of InlineKeyboardButton handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_inline_keyboard_button",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the InlineKeyboardButton event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.text (str): Label text on the button
        - update.url (str): Optional. HTTP or tg:// URL to be opened when the button is pressed. Links tg://user?id=<user_id> can be used to mention a user by their identifier without using a username, if this is allowed by their privacy settings.
        - update.callback_data (str): Optional. Data to be sent in a callback query to the bot when the button is pressed, 1-64 bytes
        - update.web_app (WebAppInfo): Optional. Description of the Web App that will be launched when the user presses the button. The Web App will be able to send an arbitrary message on behalf of the user using the method answerWebAppQuery. Available only in private chats between a user and the bot. Not supported for messages sent on behalf of a Telegram Business account.
        - update.login_url (LoginUrl): Optional. An HTTPS URL used to automatically authorize the user. Can be used as a replacement for the Telegram Login Widget.
        - update.switch_inline_query (str): Optional. If set, pressing the button will prompt the user to select one of their chats, open that chat and insert the bot's username and the specified inline query in the input field. May be empty, in which case just the bot's username will be inserted. Not supported for messages sent on behalf of a Telegram Business account.
        - update.switch_inline_query_current_chat (str): Optional. If set, pressing the button will insert the bot's username and the specified inline query in the current chat's input field. May be empty, in which case only the bot's username will be inserted.This offers a quick way for the user to open your bot in inline mode in the same chat - good for selecting something from multiple options. Not supported in channels and for messages sent on behalf of a Telegram Business account.
        - update.switch_inline_query_chosen_chat (SwitchInlineQueryChosenChat): Optional. If set, pressing the button will prompt the user to select one of their chats of the specified type, open that chat and insert the bot's username and the specified inline query in the input field. Not supported for messages sent on behalf of a Telegram Business account.
        - update.copy_text (CopyTextButton): Optional. Description of the button that copies the specified text to the clipboard.
        - update.callback_game (CallbackGame): Optional. Description of the game that will be launched when the user presses the button.NOTE: This type of button must always be the first button in the first row.
        - update.pay (bool): Optional. Specify True, to send a Pay button. Substrings "" and "XTR" in the buttons's text will be replaced with a Telegram Star icon.NOTE: This type of button must always be the first button in the first row and can only be used in invoice messages.
        """
        # Example implementation
        # Implement your handler logic here
        pass
