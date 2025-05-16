from surfgram.types import BotShortDescription
from typing import Callable


class ExampleBotShortDescription(BotShortDescription):
    """Example implementation of BotShortDescription handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_bot_short_description",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the BotShortDescription event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.short_description (str): The bot's short description
        """
        # Example implementation
        # Implement your handler logic here
        pass
