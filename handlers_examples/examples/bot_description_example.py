from surfgram.types import BotDescription
from typing import Callable


class ExampleBotDescription(BotDescription):
    """Example implementation of BotDescription handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_bot_description",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the BotDescription event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.description (str): The bot's description
        """
        # Example implementation
        # Implement your handler logic here
        pass
