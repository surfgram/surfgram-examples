from surfgram.types import BotCommand
from typing import Callable


class ExampleBotCommand(BotCommand):
    """Example implementation of BotCommand handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_bot_command",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the BotCommand event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.command (str): Text of the command; 1-32 characters. Can contain only lowercase English letters, digits and underscores.
        - update.description (str): Description of the command; 1-256 characters.
        """
        # Example implementation
        # Implement your handler logic here
        pass
