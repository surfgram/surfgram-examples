from surfgram.types import BackgroundFillSolid
from typing import Callable


class ExampleBackgroundFillSolid(BackgroundFillSolid):
    """Example implementation of BackgroundFillSolid handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_background_fill_solid",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the BackgroundFillSolid event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the background fill, always "solid"
        - update.color (int): The color of the background fill in the RGB24 format
        """
        # Example implementation
        # Implement your handler logic here
        pass
