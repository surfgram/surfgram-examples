from surfgram.types import BotCommandScopeAllPrivateChats
from typing import Callable


class ExampleBotCommandScopeAllPrivateChats(BotCommandScopeAllPrivateChats):
    """Example implementation of BotCommandScopeAllPrivateChats handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_bot_command_scope_all_private_chats",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the BotCommandScopeAllPrivateChats event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Scope type, must be all_private_chats
        """
        # Example implementation
        # Implement your handler logic here
        pass
