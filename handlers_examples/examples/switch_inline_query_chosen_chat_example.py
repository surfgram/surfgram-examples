from surfgram.types import SwitchInlineQueryChosenChat
from typing import Callable


class ExampleSwitchInlineQueryChosenChat(SwitchInlineQueryChosenChat):
    """Example implementation of SwitchInlineQueryChosenChat handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_switch_inline_query_chosen_chat",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the SwitchInlineQueryChosenChat event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.query (str): Optional. The default inline query to be inserted in the input field. If left empty, only the bot's username will be inserted
        - update.allow_user_chats (bool): Optional. True, if private chats with users can be chosen
        - update.allow_bot_chats (bool): Optional. True, if private chats with bots can be chosen
        - update.allow_group_chats (bool): Optional. True, if group and supergroup chats can be chosen
        - update.allow_channel_chats (bool): Optional. True, if channel chats can be chosen
        """
        # Example implementation
        # Implement your handler logic here
        pass
