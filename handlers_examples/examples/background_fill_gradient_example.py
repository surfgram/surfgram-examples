from surfgram.types import BackgroundFillGradient
from typing import Callable


class ExampleBackgroundFillGradient(BackgroundFillGradient):
    """Example implementation of BackgroundFillGradient handler"""

    @property
    def __names__(self) -> List[str]:
        """List of trigger names for this handler"""
        return [
            "example_background_fill_gradient",
        ]

    @property
    def __callback__(self) -> Callable:
        """Returns the handler function"""
        return self.handle

    async def handle(self, update, bot):
        """Processes the BackgroundFillGradient event

                Args:
                    update: Incoming update object
                    bot: Bot instance for making API calls

                Example fields available:
        - update.type (str): Type of the background fill, always "gradient"
        - update.top_color (int): Top color of the gradient in the RGB24 format
        - update.bottom_color (int): Bottom color of the gradient in the RGB24 format
        - update.rotation_angle (int): Clockwise rotation angle of the background fill in degrees; 0-359
        """
        # Example implementation
        # Implement your handler logic here
        pass
