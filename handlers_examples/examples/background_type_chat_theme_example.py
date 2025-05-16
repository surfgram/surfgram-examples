from surfgram.types import BackgroundTypeChatTheme
from typing import Callable


class ExampleBackgroundTypeChatTheme(BackgroundTypeChatTheme):
    """Example implementation of BackgroundTypeChatTheme handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_background_type_chat_theme",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the BackgroundTypeChatTheme event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the background, always "chat_theme"
        - update.theme_name (str): Name of the chat theme, which is usually an emoji
        """
        # Example implementation
        # Implement your handler logic here
        pass
