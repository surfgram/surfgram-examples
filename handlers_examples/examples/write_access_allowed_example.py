from surfgram.types import WriteAccessAllowed
from typing import Callable


class ExampleWriteAccessAllowed(WriteAccessAllowed):
    """Example implementation of WriteAccessAllowed handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_write_access_allowed",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the WriteAccessAllowed event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.from_request (bool): Optional. True, if the access was granted after the user accepted an explicit request from a Web App sent by the method requestWriteAccess
        - update.web_app_name (str): Optional. Name of the Web App, if the access was granted when the Web App was launched from a link
        - update.from_attachment_menu (bool): Optional. True, if the access was granted when the bot was added to the attachment or side menu
        """
        # Example implementation
        # Implement your handler logic here
        pass
