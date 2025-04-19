from surfgram.types import BotName
from typing import Callable


class ExampleBotName(BotName):
    """Example implementation of BotName handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_bot_name",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the BotName event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.name (str): The bot's name
        """
        # Example implementation
        # Implement your handler logic here
        pass
