from surfgram.types import BackgroundTypeFill
from typing import Callable


class ExampleBackgroundTypeFill(BackgroundTypeFill):
    """Example implementation of BackgroundTypeFill handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_background_type_fill",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the BackgroundTypeFill event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the background, always "fill"
        - update.fill (BackgroundFill): The background fill
        - update.dark_theme_dimming (int): Dimming of the background in dark themes, as a percentage; 0-100
        """
        # Example implementation
        # Implement your handler logic here
        pass
