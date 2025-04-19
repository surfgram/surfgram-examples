from surfgram.types import BotCommandScopeChatMember
from typing import Callable


class ExampleBotCommandScopeChatMember(BotCommandScopeChatMember):
    """Example implementation of BotCommandScopeChatMember handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_bot_command_scope_chat_member",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the BotCommandScopeChatMember event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Scope type, must be chat_member
        - update.chat_id (Union[int, str]): Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)
        - update.user_id (int): Unique identifier of the target user
        """
        # Example implementation
        # Implement your handler logic here
        pass
