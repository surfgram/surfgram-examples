from surfgram.types import WebAppData
from typing import Callable


class ExampleWebAppData(WebAppData):
    """Example implementation of WebAppData handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_web_app_data",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the WebAppData event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.data (str): The data. Be aware that a bad client can send arbitrary data in this field.
        - update.button_text (str): Text of the web_app keyboard button from which the Web App was opened. Be aware that a bad client can send arbitrary data in this field.
        """
        # Example implementation
        # Implement your handler logic here
        pass
