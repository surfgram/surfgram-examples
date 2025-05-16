from surfgram.types import BotCommandScopeDefault
from typing import Callable


class ExampleBotCommandScopeDefault(BotCommandScopeDefault):
    """Example implementation of BotCommandScopeDefault handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_bot_command_scope_default",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the BotCommandScopeDefault event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Scope type, must be default
        """
        # Example implementation
        # Implement your handler logic here
        pass
