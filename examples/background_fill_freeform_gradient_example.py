from surfgram.types import BackgroundFillFreeformGradient
from typing import Callable


class ExampleBackgroundFillFreeformGradient(BackgroundFillFreeformGradient):
    """Example implementation of BackgroundFillFreeformGradient handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_background_fill_freeform_gradient",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the BackgroundFillFreeformGradient event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the background fill, always "freeform_gradient"
        - update.colors (List[int]): A list of the 3 or 4 base colors that are used to generate the freeform gradient in the RGB24 format
        """
        # Example implementation
        # Implement your handler logic here
        pass
