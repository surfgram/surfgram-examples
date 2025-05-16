from surfgram.types import MenuButtonDefault
from typing import Callable


class ExampleMenuButtonDefault(MenuButtonDefault):
    """Example implementation of MenuButtonDefault handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_menu_button_default",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the MenuButtonDefault event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the button, must be default
        """
        # Example implementation
        # Implement your handler logic here
        pass
