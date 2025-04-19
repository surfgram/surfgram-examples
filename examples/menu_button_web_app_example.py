from surfgram.types import MenuButtonWebApp
from typing import Callable


class ExampleMenuButtonWebApp(MenuButtonWebApp):
    """Example implementation of MenuButtonWebApp handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_menu_button_web_app",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the MenuButtonWebApp event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the button, must be web_app
        - update.text (str): Text on the button
        - update.web_app (WebAppInfo): Description of the Web App that will be launched when the user presses the button. The Web App will be able to send an arbitrary message on behalf of the user using the method answerWebAppQuery. Alternatively, a t.me link to a Web App of the bot can be specified in the object instead of the Web App's URL, in which case the Web App will be opened as if the user pressed the link.
        """
        # Example implementation
        # Implement your handler logic here
        pass
