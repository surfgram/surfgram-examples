from surfgram.types import UniqueGiftBackdropColors
from typing import Callable


class ExampleUniqueGiftBackdropColors(UniqueGiftBackdropColors):
    """Example implementation of UniqueGiftBackdropColors handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_unique_gift_backdrop_colors",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the UniqueGiftBackdropColors event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.center_color (int): The color in the center of the backdrop in RGB format
        - update.edge_color (int): The color on the edges of the backdrop in RGB format
        - update.symbol_color (int): The color to be applied to the symbol in RGB format
        - update.text_color (int): The color for the text on the backdrop in RGB format
        """
        # Example implementation
        # Implement your handler logic here
        pass
