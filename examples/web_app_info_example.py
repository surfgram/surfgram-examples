from surfgram.types import WebAppInfo
from typing import Callable


class ExampleWebAppInfo(WebAppInfo):
    """Example implementation of WebAppInfo handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_web_app_info",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the WebAppInfo event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.url (str): An HTTPS URL of a Web App to be opened with additional data as specified in Initializing Web Apps
        """
        # Example implementation
        # Implement your handler logic here
        pass
