from surfgram.types import BotCommandScopeAllChatAdministrators
from typing import Callable


class ExampleBotCommandScopeAllChatAdministrators(BotCommandScopeAllChatAdministrators):
    """Example implementation of BotCommandScopeAllChatAdministrators handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_bot_command_scope_all_chat_administrators",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the BotCommandScopeAllChatAdministrators event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Scope type, must be all_chat_administrators
        """
        # Example implementation
        # Implement your handler logic here
        pass
